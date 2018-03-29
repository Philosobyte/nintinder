from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name = 'settings'),
    path('achievements/', views.achievements, name = 'achievements'),
    path('matches/', views.matches, name = 'matches'),
]