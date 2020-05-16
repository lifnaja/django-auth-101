from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'commons/profile.html'
