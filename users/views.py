from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login

from users.forms import CustomLoginForm,CustomUserCreationForm
class CustomLoginView(LoginView):
    template_name= 'users/login3.html'
    authentication_form = CustomLoginForm

class RegisterView(SuccessMessageMixin,CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = "Registration successful! Please login"

    def form_invalid(self, form):
        # Print form errors to console for debugging
        print("Form errors:", form.errors)
        messages.error(self.request, f"Registration failed: {form.errors}")
        return super().form_invalid(form)

    def form_valid(self, form):
        # Print success message
        print("Form is valid, saving user...")
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)