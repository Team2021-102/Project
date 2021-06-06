from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Generator
from django.forms import ModelForm, TextInput, Textarea


class DrawForm(forms.Form):
    file = open("main/files/draws.txt", 'r', encoding="utf-8")
    draws = file.readlines()
    file.close()


class EatForm(forms.Form):
    file = open("main/files/eats.txt", 'r', encoding="utf-8")
    eats = file.readlines()
    file.close()


class ListenForm(forms.Form):
    file = open("main/files/listens.txt", 'r', encoding="utf-8")
    listens = file.readlines()
    file.close()


class PlayForm(forms.Form):
    file = open("main/files/plays.txt", 'r', encoding="utf-8")
    plays = file.readlines()
    file.close()


class WatchForm(forms.Form):
    file = open("main/files/watches.txt", 'r', encoding="utf-8")
    watches = file.readlines()
    file.close()


class DoingForm(forms.Form):
    file = open("main/files/doings.txt", 'r', encoding="utf-8")
    doings = file.readlines()
    file.close()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),

        }


class GeneratorForm(ModelForm):
    class Meta:
        model = Generator
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'input-name',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'input-element',
                'placeholder': 'Введите значения через запятую'
            }),
        }