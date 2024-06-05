from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label='your password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='repeat your password')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email is already in use')
        return email


class ProfileEditForm(forms.ModelForm):
    email = forms.CharField(disabled=True, widget=forms.TextInput)

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location', 'email']
