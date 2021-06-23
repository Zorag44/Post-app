from django.contrib import admin
from django.urls import path,include
from blog1 import views
from django.contrib.auth import views as auth_views
from .views import postlistview,postcreateview
urlpatterns = [
    path('', postlistview.as_view(),name="blog1_index"),
    path('about', views.about,name="blog1_ABOUT"),
    path('register',views.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='blog1/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='blog1/logout.html'),name='logout'),
    path('profile',views.profile,name='profile'),
    path('post/new',postcreateview.as_view(),name='post_create'),
    path('sumpott', views.sumpott,name='sumpott')
]
