import random

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import FormView, CreateView
from .forms import DrawForm, PlayForm, DoingForm, WatchForm, ListenForm, EatForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def login1(request):
    return render(request, 'main/index-log.html')


def registration1(request):
    return render(request, 'main/index-reg.html')


def main(request):
    return render(request, 'main/main-page.html')


def profile(request):
    return render(request, 'main/exit.html')


def tasks(request):
    return render(request, 'main/tasks.html')


def donate(request):
    return render(request, 'main/donate.html')


def other(request):
    return render(request, 'main/other.html')


def listen(request):
    current_thing = ''
    if request.GET.get('click'):
        rand = random.uniform(0, len(ListenForm.listens))
        rand = int(rand)
        current_thing = ListenForm.listens[rand]
    return render(request, 'main/listen.html', {'current_thing': current_thing})


def watch(request):
    current_thing = ''
    if request.GET.get('click'):
        rand = random.uniform(0, len(WatchForm.watches))
        rand = int(rand)
        current_thing = WatchForm.watches[rand]
    return render(request, 'main/watch.html', {'current_thing': current_thing})


def play(request):
    current_thing = ''
    if request.GET.get('click'):
        rand = random.uniform(0, len(PlayForm.plays))
        rand = int(rand)
        current_thing = PlayForm.plays[rand]
    return render(request, 'main/play.html', {'current_thing': current_thing})


def doing(request):
    current_thing = ''
    if request.GET.get('click'):
        rand = random.uniform(0, len(DoingForm.doings))
        rand = int(rand)
        current_thing = DoingForm.doings[rand]
    return render(request, 'main/doing.html', {'current_thing': current_thing})


def eat(request):
    current_thing = ''
    if request.GET.get('click'):
        rand = random.uniform(0, len(EatForm.eats))
        rand = int(rand)
        current_thing = EatForm.eats[rand]
    return render(request, 'main/eat.html', {'current_thing': current_thing})


def draw(request):
    current_thing = ''
    if request.GET.get('click'):
        rand = random.uniform(0, len(DrawForm.draws))
        rand = int(rand)
        current_thing = DrawForm.draws[rand]
    return render(request, 'main/draw.html', {'current_thing': current_thing})


def create(request):
    return render(request, 'main/create.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/index-reg.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/index-log.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

