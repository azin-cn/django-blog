from django.http import HttpResponse
from django.shortcuts import render
from article.models import Article, Tag


# Create your views here.
# 首页
def index(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    dict = {'articles':articles,'tags':tags}
    return render(request, 'article/index.html',dict)

def tag(request,name):
    tag = Tag.objects.get(tag=name)
    # 注意多表查询
    # http: // www.loonapp.com / blog / 3 /
    articles_with_tag = tag.article_set.all()
    # 如果存在相应的文章
    # articles_with_tag.count() != 0
    if articles_with_tag.exists():
        # articles_with_tag 是对象集合
        return render(request,'article/articles_with_tag.html',{'articles_with_tag':articles_with_tag})
    else:
        HttpResponse.status_code = 404
        return render(request, '404.html')

# 搜素
def search(request,keyword):
    pass

# 详情
def detail(request,id):
    # 这里可以使用filter函数，返回的是对象的集合，需要取出对象在拿字段的值，get函数返回的是一个对象
    # article = Article.objects.filter(id=id)[0]
    try:
        article = Article.objects.get(id=id)
        print(article.title)
    except :
        return render(request,'404.html')
    return render(request,'article/detail.html',{'article':article})