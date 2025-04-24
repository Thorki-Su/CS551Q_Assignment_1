from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SearchForm(forms.Form):
    input = forms.CharField(
        label='Country Name or Code',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter name or code'})
    )

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
