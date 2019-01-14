from django import forms
from .models import Task

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'group', 'user', )
