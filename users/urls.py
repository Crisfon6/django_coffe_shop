from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import CustomLoginView, RegisterView

urlpatterns = [
    # path('login/',LoginView.as_view(template_name="users/login.html"), name="login"),
    # path('login2/',LoginView.as_view(template_name="users/login2.html"), name="login2"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
