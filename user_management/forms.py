from django import forms
from user_management import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['email', 'username', 'password']
        labels = {
            'email': '',
            'username': '',
            'password': ''
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address (Private)',
                'id': 'email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username (Public)',
                'id': 'username',
                'readonly': True
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password (Private)'
            }),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = []
