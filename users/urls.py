from django.urls import path
from django.contrib.auth.views import LoginView 
from users.views import CustomLoginView

urlpatterns = [
    path('login/',LoginView.as_view(template_name="users/login.html"), name="login"),
    path('login2/',LoginView.as_view(template_name="users/login2.html"), name="login2"),
    path('login3',CustomLoginView.as_view(), name="login3"),
]