from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from ..models import ClubRegistration, ClubType, EventLocation, ClubSchedule, Teacher, Weekday, Booking
import datetime


class ClubRegistrationForm(ModelForm):
    class Meta:
        model = ClubRegistration
        fields = "__all__"

    name = forms.CharField(max_length=255, label="Название кружка", widget=forms.TextInput(attrs={'size': 80}))
    datetime = forms.DateTimeField(label="Дата начала работы кружка", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format="%Y-%m-%dT%H:%M"))
    type = forms.ModelChoiceField(ClubType.objects.all(), label="Вид кружка")
    locations = forms.ModelMultipleChoiceField(EventLocation.objects.all(), label="Помещение")
    schedule_type = forms.ChoiceField(choices=ClubRegistration.ScheduleTypeEnum.choices, label="Вариант расписания", widget=forms.Select(attrs={'onchange': 'schedule_type_onchange();'}))
    teacher = forms.ModelChoiceField(Teacher.objects.all(), label="Преподаватель")

    schedule_day_1 = forms.ModelChoiceField(queryset=Weekday.objects.all(), label="День", required=False, widget=forms.Select(attrs={'onchange': 'schedule_day_1_onchange();'}))
    schedule_time_start_1 = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="время начала занятий", required=False)
    schedule_time_end_1 = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="время окончания занятий", required=False)

    schedule_day_2 = forms.ModelChoiceField(queryset=Weekday.objects.all(), label="День", required=False, widget=forms.Select(attrs={'onchange': 'schedule_day_2_onchange();'}))
    schedule_time_start_2 = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="время начала занятий", required=False)
    schedule_time_end_2 = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="время окончания занятий", required=False)

    schedule_day_3 = forms.ModelChoiceField(queryset=Weekday.objects.all(), label="День", required=False, widget=forms.Select(attrs={'onchange': 'schedule_day_3_onchange();'}))
    schedule_time_start_3 = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="время начала занятий", required=False)
    schedule_time_end_3 = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="время окончания занятий", required=False)

    def clean(self):
        def check_booking_intersection(check_date_start, check_date_end):
            booking = Booking.objects.filter(
                locations__id__in=[x.id for x in self.cleaned_data["locations"]]
            ).filter(date_end__gt=self.cleaned_data["datetime"]).distinct()

            result = []

            for b in booking:
                date_start = datetime.datetime(1, 1, b.date_start.weekday() + 1, b.date_start.hour, b.date_start.minute, b.date_start.second)
                date_end = datetime.datetime(1, 1, b.date_end.weekday() + 1, b.date_end.hour, b.date_end.minute, b.date_end.second)

                if date_start > check_date_end:
                    continue

                if date_end < check_date_start:
                    continue

                result.append(b)

            return len(result) == 0

        def check_club_schedule_intersection(check_date_start, check_date_end, adding):
            schedule = ClubRegistration.get_club_schedule_intersection(
                [x.id for x in self.cleaned_data["locations"]],
                check_date_start,
                check_date_end
            )

            return len(schedule) == 0 if adding else len(schedule) == 1

        if self.cleaned_data["schedule_type"] in '123':
            if self.cleaned_data["schedule_day_1"] is None or\
               self.cleaned_data["schedule_time_start_1"] is None or \
               self.cleaned_data["schedule_time_end_1"] is None:
                raise ValidationError("Не все поля заполнены.")

            date_start = datetime.datetime.combine(datetime.date(1, 1, self.cleaned_data["schedule_day_1"].id), self.cleaned_data["schedule_time_start_1"])
            date_end = datetime.datetime.combine(datetime.date(1, 1, self.cleaned_data["schedule_day_1"].id),
                                                   self.cleaned_data["schedule_time_end_1"])

            if not check_booking_intersection(date_start, date_end):
                raise ValidationError("Расписание кружка пересекается с бронированием.")

            if not check_club_schedule_intersection(date_start, date_end, self.instance._state.adding):
                raise ValidationError("Расписание кружка пересекается с другим кружком.")

        if self.cleaned_data["schedule_type"] in '23':
            if self.cleaned_data["schedule_day_2"] is None or\
               self.cleaned_data["schedule_time_start_2"] is None or \
               self.cleaned_data["schedule_time_end_2"] is None:
                raise ValidationError("Не все поля заполнены.")

            date_start = datetime.datetime.combine(datetime.date(1, 1, self.cleaned_data["schedule_day_2"].id),
                                                   self.cleaned_data["schedule_time_start_2"])
            date_end = datetime.datetime.combine(datetime.date(1, 1, self.cleaned_data["schedule_day_2"].id),
                                                 self.cleaned_data["schedule_time_end_2"])

            if not check_booking_intersection(date_start, date_end):
                raise ValidationError("Расписание кружка пересекается с бронированием.")

            if not check_club_schedule_intersection(date_start, date_end, self.instance._state.adding):
                raise ValidationError("Расписание кружка пересекается с другим кружком.")

        if self.cleaned_data["schedule_type"] in '3':
            if self.cleaned_data["schedule_day_3"] is None or\
               self.cleaned_data["schedule_time_start_3"] is None or \
               self.cleaned_data["schedule_time_end_3"] is None:
                raise ValidationError("Не все поля заполнены.")

            date_start = datetime.datetime.combine(datetime.date(1, 1, self.cleaned_data["schedule_day_3"].id),
                                                   self.cleaned_data["schedule_time_start_3"])
            date_end = datetime.datetime.combine(datetime.date(1, 1, self.cleaned_data["schedule_day_3"].id),
                                                 self.cleaned_data["schedule_time_end_3"])

            if not check_booking_intersection(date_start, date_end):
                raise ValidationError("Расписание кружка пересекается с бронированием.")

            if not check_club_schedule_intersection(date_start, date_end, self.instance._state.adding):
                raise ValidationError("Расписание кружка пересекается с другим кружком.")

        return self.cleaned_data

    def save(self, commit=True):
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate."
                % (
                    self.instance._meta.object_name,
                    "created" if self.instance._state.adding else "changed",
                )
            )

        if not self.instance._state.adding:
            for s in self.instance.schedule.all():
                 s.delete()

        schedule = [ClubSchedule(
            weekday=self.cleaned_data["schedule_day_1"],
            time_start=self.cleaned_data["schedule_time_start_1"],
            time_end=self.cleaned_data["schedule_time_end_1"]
        )]

        if self.cleaned_data["schedule_day_2"] is not None:
            schedule.append(ClubSchedule(
                weekday=self.cleaned_data["schedule_day_2"],
                time_start=self.cleaned_data["schedule_time_start_2"],
                time_end=self.cleaned_data["schedule_time_end_2"]
            ))

        if self.cleaned_data["schedule_day_3"] is not None:
            schedule.append(ClubSchedule(
                weekday=self.cleaned_data["schedule_day_3"],
                time_start=self.cleaned_data["schedule_time_start_3"],
                time_end=self.cleaned_data["schedule_time_end_3"]
            ))

        for s in schedule:
            s.save()

        self.instance.save()

        self.instance.schedule.set(schedule)

        if commit:
            self._save_m2m()
        else:
            self.save_m2m = self._save_m2m
        return self.instance
