from django.contrib import admin
from . models import UserProfile
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)
# admin.site.unregister(User)

admin.site.register(UserProfile)