from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Content(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    content = models.FileField()


    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateTimeField()
    city = models.CharField(max_length=50)
    phone = PhoneNumberField()
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)



