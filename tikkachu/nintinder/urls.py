from django.conf.urls import include, url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name = 'settings'),
    path('achievements/', views.achievements, name = 'achievements'),
    url(r'achievements/earn/', views.earn_achievement, name="earn_achievement"),
    path('achievements/create/', views.AchievementCreate.as_view(), name='achievements_create'),
    path('matches/', views.matches, name = 'matches'),
]
