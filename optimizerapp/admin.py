from django.contrib import admin
from .models import Developer_info , UserProfile
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Developer_info)

admin.site.register(UserProfile)
