from django.urls import path
from django.contrib.auth import views as auth_views

from . import views



urlpatterns=[
    path('users/register/',
        views.user_register,
        name='register'),
        
    path('users/login/',
        views.user_login,
        name='login'),
        
    path('users/profile/',
        views.user_profile,
        name='profile'),
        
    path('users/profile/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'),
        
        
        
        
    path('admins/users/get',
        views.get_users,
        name='get_users'),
        
    path('admins/users/edit/<pk>',
        views.edit_user,
        name='edit_user'),
        
    path('admins/users/delete/<pk>',
        views.delete_user,
        name='delete_user'),
    ]
