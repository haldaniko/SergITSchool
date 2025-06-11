from django.core.exceptions import ValidationError
from django.db import models


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Име")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Име на събитието")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    start_date = models.DateField(verbose_name="Начална дата")
    end_date = models.DateField(verbose_name="Крайна дата")
    start_time = models.TimeField(verbose_name="Дата на отваряне")
    end_time = models.TimeField(verbose_name="Дата на затваряне")
    location = models.CharField(max_length=255, verbose_name="Място на провеждане")

    def __str__(self):
        return (f"{self.title} — от {self.start_date.strftime('%d.%m.%Y %H:%M')} "
                f"до {self.end_date.strftime('%d.%m.%Y %H:%M')}")

    def clean(self):
        super().clean()
        if self.end_date < self.start_date:
            raise ValidationError("Крайната дата трябва да е след началната дата.")