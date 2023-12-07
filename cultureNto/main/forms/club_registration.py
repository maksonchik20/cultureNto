from django import forms
from django.forms import ModelForm
from ..models import ClubRegistration, ClubType, EventLocation, ClubSchedule, Teacher


class ClubRegistrationForm(ModelForm):
    class Meta:
        model = ClubRegistration
        fields = "__all__"

    name = forms.CharField(max_length=255, label="Название кружка")
    datetime = forms.DateTimeField(label="Дата начала работы кружка", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    type = forms.ModelChoiceField(ClubType.objects.all(), label="Вид кружка")
    locations = forms.ModelMultipleChoiceField(EventLocation.objects.all(), label="Помещение")
    schedule_type = forms.ChoiceField(choices=ClubRegistration.ScheduleTypeEnum.choices, label="Вариант расписания")
    schedule = forms.ModelMultipleChoiceField(ClubSchedule.objects.all(), label="Расписание")
    teacher = forms.ModelChoiceField(Teacher.objects.all(), label="Преподаватель")

    def clean(self):
        return self.cleaned_data
