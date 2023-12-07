from django.db import models


class Teacher(models.Model):
    last_name = models.CharField(max_length=60, verbose_name="Фамилия")
    first_name = models.CharField(max_length=60, verbose_name="Имя")
    middle_name = models.CharField(max_length=60, verbose_name="Отчество")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
