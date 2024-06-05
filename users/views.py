from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from users.forms import UserRegisterForm, ProfileEditForm
from users.models import Profile, User


class DeleteProfile(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_profile.html'
    success_url = reverse_lazy('index')


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
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})


def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user, email=user.email)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form': form})
