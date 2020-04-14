from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up', views.register, name='register'),
    path('login', views.user_login, name='user_login'),
]
