from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class ModelAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'date_of_birth', 'profile_photo']

admin.site.register(CustomUser, CustomUserAdmin)