import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, ProfileForm
from users.models import User
from users.services import send_mail


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class LogoutView(BaseLogoutView):
    pass

class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            _to_mail=new_user.email,
            _message='Поздравляю, вы зарегистрировались на нашем сайте!',
            _subject='Верификация'
        )
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('users:profile')
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0,9)) for _ in range(12)])
    send_mail(
        _to_mail=request.user.email,
        _subject=f'Password: {new_password}',
        _message=request.user.email
    )

    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))