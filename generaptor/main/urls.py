from django.urls import path
from . import views
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('login', LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('registration', RegisterUser.as_view(), name='registration'),
    path('', views.main, name='home'),
    path('exit', views.profile, name='exit'),
    path('tasks', views.tasks, name='tasks'),
    path('donate', views.donate, name='donate'),
    path('other', views.other, name='other'),
    path('listen', views.listen, name='listen'),
    path('play', views.play, name='play'),
    path('watch', views.watch, name='watch'),
    path('doing', views.doing, name='doing'),
    path('eat', views.eat, name='eat'),
    path('draw', views.draw, name='draw'),
    path('create', views.create, name='create'),
]
