from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
