from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<user_profile>', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name = 'settings'),
    path('achievements/', views.achievements, name = 'achievements'),
    path('signup/', views.sign_up, name='sign_up'),
    url(r'achievements/earn/', views.earn_achievement, name="earn_achievement"),
    url(r'signup/$', views.sign_up, name='signup'),
    path('games/', views.games, name='games'),
    path('interest/add', views.add_interest, name='add_interest'),
    path('matches/', views.matches, name='matches'),
]
