from django.contrib.auth.views import LoginView

from users.forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name= 'users/login3.html'
    authentication_form = CustomLoginForm
    