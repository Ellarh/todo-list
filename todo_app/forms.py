from django import forms
from django.contrib.auth.models import User
from .models import TodoList


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task_date', 'task', 'task_is_done']

