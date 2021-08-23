import extra_apps.xadmin as xadmin
from apps.article.models import *
from django.contrib.auth.models import User
from apps.article.models import Article, Category, Tag
# Register your models here

# list_display, search_fields, list_filter
# 注册后台


class ArticleAdmin(object):
    list_filter = ['created','updated']
    search_fields = ['title','content','category','tag']
    list_display = ['title','author','category','updated']
    style_fields = {'tag': 'checkbox-inline', }
xadmin.site.register(Article,ArticleAdmin)

class CategoryAdmin(object):
    list_diaplay = ['created','category',]
    search_fields = ['category','created']
    list_filter = ['created', ]
xadmin.site.register(Category,CategoryAdmin)

class TagAdmin(object):
    list_diplay = ['created','tag',]
    search_fields = ['tag','created']
    list_filter = ['created', ]
xadmin.site.register(Tag,TagAdmin)

class NavigationAdmin(object):
    list_display = ['nav','url']
xadmin.site.register(Navigation,NavigationAdmin)

#DjangoUeditor detail就是要显示为富文本的字段名
# class ArticleAdmin(object):
#     style_fields = {"content": "ueditor"}
# xadmin.site.register(Article,ArticleAdmin)