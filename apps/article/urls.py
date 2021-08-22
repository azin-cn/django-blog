#coding=utf-8
from django.urls import path,include
from apps.article import views as article

# 使用关键字传参
urlpatterns=[
    path('', article.index,name='article_index'),
    path('search/',article.search,name='article_search'),
    path('detail/<int:id>/',article.detail,name='article_detail'),
    # 可以同时进行文章名的传递，需要修改的html有articles_with_tag_or_category_or_search和index，
    # 需要修改的函数为detail函数
    # path('detail/<int:id>/<str:name>',article.detail,name='article_detail'),
    path('tag/<str:name>/',article.tag,name='article_tag'),
    path('category/<str:name>/',article.category,name='article_category')
]