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
    url(r'friend/all/', views.get_friends, name='get_friends'),
    url(r'friend/add/', views.add_friend, name='add_friend'),
    url(r'friend/remove/', views.remove_friend, name='remove_friend'),
    url(r'friend/blacklist/', views.blacklist_friend, name='blacklist_friend'),
    url(r'signup/$', views.sign_up, name='signup')
    # url(r'password_reset/', auth_views.password_reset, name='password_reset'),
    # url(r'password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    
    # path('achievements/create/', views.AchievementCreate.as_view(), name='achievements_create'),
    # path('game/add', views.InterestCreate.as_view(), name='interests_create'),
    # path('matches/', views.matches, name = 'matches'),
]
