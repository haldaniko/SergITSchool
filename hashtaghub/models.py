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
    datetime = models.DateTimeField(verbose_name="Дата и час")
    location = models.CharField(max_length=255, verbose_name="Място на провеждане")

    def __str__(self):
        return f"{self.title} — {self.datetime.strftime('%d.%m.%Y %H:%M')}"
