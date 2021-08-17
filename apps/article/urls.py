#coding=utf-8
from django.urls import path,include
from article import views as article

# 使用关键字传参
urlpatterns=[
    path('', article.index,name='article_index'),
    path('search/<str:keyword>',article.search,name='article_search'),
    path('detail/<int:id>',article.detail,name='article_detail'),
    path('tag/<str:name>',article.tag,name='article_tag'),
]