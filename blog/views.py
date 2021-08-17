# coding=utf-8
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate


def feedback(request):
    return HttpResponse('留言反馈')

def login(request):
    return HttpResponse('登录')


def dropdown(request):
    return HttpResponse('注销')


def register(request):
    return HttpResponse('注册')
