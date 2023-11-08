from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PhoneNumber(models.Model):
    phone = models.CharField(max_length=12,unique=True)


# models.py

class Receive(models.Model):
    msg=models.CharField(max_length=200)
    uid=models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)  # Add timestamp field

    def __str__(self):
        return self.msg


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.phone_number})"

# myapp/models.py


class Message(models.Model):
   
    msg = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)  # Add timestamp field

    def __str__(self):
        return self.msg
    # timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"Message at {self.timestamp}"
