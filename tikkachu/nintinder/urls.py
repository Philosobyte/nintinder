from django.conf.urls import include, url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('profile/(?P<user_profile>[-\w]+)', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name = 'settings'),
    path('achievements/', views.achievements, name = 'achievements'),
    url(r'achievements/earn/', views.earn_achievement, name="earn_achievement"),
    url(r'friend/all/', views.get_friends, name='get_friends'),
    url(r'friend/add/', views.add_friend, name='add_friend'),
    url(r'friend/remove/', views.remove_friend, name='remove_friend'),
    url(r'friend/blacklist/', views.blacklist_friend, name='blacklist_friend'),
    path('games/', views.games, name='games'),
    path('interest/add', views.add_interest, name='add_interest'),
    # path('achievements/create/', views.AchievementCreate.as_view(), name='achievements_create'),
    #path('game/add', views.InterestCreate.as_view(), name='interests_create'),
    path('matches/', views.matches, name='matches'),
]
