# coding=utf-8
from datetime import datetime

from apps.article.models import Tag, Category, Article, Navigation


# 定义全局变量，在setting中进行添加
def article_global_var(request):
    # 取出最新文章的前五条数据，不足五条，全部取出
    tags = Tag.objects.all()
    categories = Category.objects.all()
    latestArticles = Article.objects.all()
    navigations = Navigation.objects.all()
    title = 'LuckyDog幸运儿'
    copyright = '© %s %s'%(datetime.now().year,title)
    beian = '粤ICP备2020137256号-1'
    if latestArticles.count()>=5:
        latestArticles =  latestArticles[:5]
    if tags.count() >= 4:
        categories = categories[:4]
    if navigations.count()>=4:
        navigations = navigations[:4]
    dict = {'latestArticles':latestArticles,'categories':categories,
            'tags':tags,'navigations':navigations,'nav_title':title,
            'copyright':copyright,'beian':beian}
    # 取出分类名称，固定为四个，但是名称不固定，所以从数据库中找出
    return dict

def navigation_var(request):
    cloud = ''
    about = ''

def feedback(request):
    pass