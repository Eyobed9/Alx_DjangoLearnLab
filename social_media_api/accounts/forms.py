from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "bio")
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "bio"]
        
