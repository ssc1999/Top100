from django.db import models
from phone_field import PhoneField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneField()
    mail = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.mail
