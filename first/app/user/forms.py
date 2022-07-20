from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        field = ('username', 'password')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='Имя')
    last_name = forms.CharField(max_length=50, label='Фамилия')
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput())
    password_confirm = forms.CharField(max_length=50, label='Подтверждение пароля', widget=forms.PasswordInput())

    class Meta:
        model = User

    def check_password_confirm(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password_confirm']