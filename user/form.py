from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']