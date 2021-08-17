#coding=utf-8
from django.http import HttpResponse


def feedback(request):
    return HttpResponse('留言反馈')