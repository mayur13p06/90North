from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import re_path
from django.contrib.staticfiles.views import serve

urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
   path('logout/', views.logout_view, name='logout'),
    re_path(r'^favicon\.ico$', serve, {'path': 'favicon.ico'}),
]