from django.contrib import admin
from .models import PhoneNumber
# Register your models here.
# admin.py
from django.contrib import admin
from .models import Message
from .models import Receive
admin.site.register(Message)
admin.site.register(Receive)
admin.site.register(PhoneNumber)