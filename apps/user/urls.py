#coding=utf-8
from django.urls import path
from apps.user import views as user

urlpatterns=[
    path('login/', user.Login.as_view(), name='user_login'),
    path('register/', user.Register.as_view(), name='user_register'),
    path('dropdown/', user.dropdown, name='user_dropdown'),
    path('forgot/',user.forgot,name='user_forgot')
]