from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, ProfileEditForm
from users.models import Profile


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class UserProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.request.user.pk])


def index(request):
    return render(request, 'index.html', {})


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user)
        return redirect('index')