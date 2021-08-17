from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from article.models import Article, Tag, Category


# Create your views here.
# 定义全局变量
def article_global_var(request):
    # 取出最新文章的前五条数据，不足五条，全部取出
    tags = Tag.objects.all()
    categories = Category.objects.all()
    latestArticles = Article.objects.all()
    if latestArticles.count()>=5:
        latestArticles =  latestArticles[:5]
    if tags.count() >= 4:
        categories = categories[:4]
    dict = {'latestArticles':latestArticles,'categories':categories,'tags':tags}
    # 取出分类名称，固定为四个，但是名称不固定，所以从数据库中找出
    return dict

# 首页
def index(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html',{'articles':articles,})

def judge_tag_category_search(request,articles_with_tag_or_category_or_search):
    # 如果存在相应的文章
    # articles_with_tag.count() != 0
    if articles_with_tag_or_category_or_search.exists():
        # 如果存在文章，那么还需要进行分页功能的实现
        return render(request, 'article/articles_with_tag_or_category_or_search.html',
                      {'articles_with_tag_or_category_or_search': articles_with_tag_or_category_or_search})
    else:
        # 设置状态码为404，默认为200，
        return render(request, '404.html', status=404)

def tag(request,name):
    # 注意多表查询
    # http: // www.loonapp.com / blog / 3 /
    # articles_with_tag_or_category_or_search 是对象集合
    try:
        tag = Tag.objects.get(tag=name)
        articles_with_tag_or_category_or_search = tag.article_set.all()
        return judge_tag_category_search(request, articles_with_tag_or_category_or_search)
    except:
        return render(request,'404.html',status=404)

def category(request,name):
    # 可以使用properties的配置文件，将耦合转移到文件的配置处
    if name == '摄影':
        return redirect('https://www.luckywords.cn/')
    try:
        category = Category.objects.get(category=name)
        articles_with_tag_or_category_or_search = category.article_set.all()
        return judge_tag_category_search(request, articles_with_tag_or_category_or_search)
    except:
        return render(request,'404.html',status=404)

# 搜素,使用get方式传递参数，而不是配置路由传递传递参数
def search(request):
    keyword = request.GET.get('keyword','')
    # print(keyword)
    # 标题或者是内容中包含关键字
    # 在组合使用条件查询时，应注意的是：使用Q查询，Q查询主要用于条件查询，而F查询主要用于更新操作
    if keyword is not None:
        articles_with_tag_or_category_or_search = Article.objects.filter(
            Q(title__contains=keyword) | Q(content__contains=keyword))
        return judge_tag_category_search(request, articles_with_tag_or_category_or_search)
    elif keyword=='':
        return render(request,'404.html',status=404)

# 详情
def detail(request, id, name):
    # 这里可以使用filter函数，返回的是对象的集合，需要取出对象在拿字段的值，get函数返回的是一个对象
    # article = Article.objects.filter(id=id)[0]
    try:
        article = Article.objects.get(id=id)
    except :
        return render(request,'404.html')
    return render(request,'article/detail.html',{'article':article})