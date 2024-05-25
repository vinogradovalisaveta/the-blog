from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users import forms
from users.models import Profile


def index(request):
    return render(request, 'index.html', {})


class UserRegisterView(CreateView):
    model = User
    form_class = forms.UserRegisterForm
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user)
        return redirect('index')


class ProfileEdit(UpdateView):
    form_class = forms.ProfileEditForm
    model = Profile
    template_name = 'profile.html'
    success_url = reverse_lazy('index')


