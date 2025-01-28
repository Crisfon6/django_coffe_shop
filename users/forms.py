from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit,HTML,ButtonHolder


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm",
                "placeholder": "Password",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # Ensure the form method is POST
        self.helper.layout = Layout(
            Field("username", css_class="mb-4"),
            Field("password", css_class="mb-4"),
            ButtonHolder(
                HTML("""
                  <button class="group relative inline-block focus:outline-none focus:ring w-full" href="#">
                    <span
                      class="absolute inset-0 translate-x-1.5 translate-y-1.5 bg-yellow-300 transition-transform group-hover:translate-x-0 group-hover:translate-y-0 w-full"
                    ></span>

                    <span
                      class="relative inline-block border-2 border-current px-8 py-3 text-sm font-bold uppercase tracking-widest text-black group-active:text-opacity-75 w-full" style="text-align:center;"
                    >
                      Login
                    </span>
                  </button>

                     """),
            ),
        )
