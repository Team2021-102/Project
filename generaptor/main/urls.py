from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('main-page', views.main, name='home'),
    path('profile', views.profile, name='profile'),
    path('tasks', views.tasks, name='tasks'),
    path('donate', views.donate, name='donate'),
    path('meow', views.meow, name='meow'),
    path('listen', views.listen, name='listen'),
    path('play', views.play, name='play'),
    path('watch', views.watch, name='watch'),
    path('doing', views.doing, name='doing'),
    path('eat', views.eat, name='eat'),
    path('draw', views.draw, name='draw'),
]
