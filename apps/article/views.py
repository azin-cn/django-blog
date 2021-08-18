from django.core.paginator import Paginator
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
    # 处理清洗过后的path，page等，特别是articles，是只含有当前页面的articles，而不是所有的复合条件的articles
    path,page,num_pages,page_obj,articles = paging(request, articles)
    context = {'path':path,'page':page,'num_pages':num_pages,'page_obj':page_obj,'articles':articles,}
    return render(request, 'article/index.html',context)

def judge_tag_category_search(request,name,path,page,num_pages,page_obj,articles):
    # 如果存在相应的文章
    # articles_with_tag.count() != 0
    # 此时的是一个page对象，而不是文章集合
    # AttributeError: 'Page' object has no attribute 'exists'
    if articles.exists():
        # 如果存在文章，那么还需要进行分页功能的实现
        data = {'name':name,'path':path,'page':page,'num_pages':num_pages,'page_obj':page_obj,
                   'articles': articles,}
        return render(request, 'article/articles_with_tag_or_category_or_search.html',data)
    else:
        # 设置状态码为404，默认为200，
        return render(request, '404.html', status=404)

def tag_category_search(request,name,articles):
    # 处理清洗过后的path，page等，特别是articles，是只含有当前页面的articles，而不是所有的复合条件的articles
    path,page, num_pages, page_obj, articles = paging(request, articles=articles)
    return judge_tag_category_search(request, name, path, page, num_pages,
                                     page_obj,articles)

def tag(request,name):
    # 注意多表查询
    # http: // www.loonapp.com / blog / 3 /
    # articles_with_tag_or_category_or_search 是对象集合
    try:
        tag = Tag.objects.get(tag=name)
        articles = tag.article_set.all()
        # 分页功能的实现，通过paging方法
        return tag_category_search(request,name,articles)
    except:
        return render(request, '404.html', status=404)

def category(request,name):
    # 可以使用properties的配置文件，将耦合转移到文件的配置处
    if name == '摄影':
        return redirect('https://www.luckywords.cn/')
    # try:
    category = Category.objects.get(category=name)
    articles = category.article_set.all()
    return tag_category_search(request,name,articles)
    # except:
    #     print('category中Error')
    #     return render(request,'404.html',status=404)

# 搜素,使用get方式传递参数，而不是配置路由传递传递参数
def search(request):
    keyword = request.GET.get('keyword','')
    # print(keyword)
    # 标题或者是内容中包含关键字
    # 在组合使用条件查询时，应注意的是：使用Q查询，Q查询主要用于条件查询，而F查询主要用于更新操作
    if keyword is not None:
        articles = Article.objects.filter(
            Q(title__contains=keyword) | Q(content__contains=keyword))
        return tag_category_search(request,'Serach - '+keyword,articles)
    elif keyword=='':
        return render(request,'404.html',status=404)

# 详情
def detail(request, id):
    # 这里可以使用filter函数，返回的是对象的集合，需要取出对象在拿字段的值，get函数返回的是一个对象
    # article = Article.objects.filter(id=id)[0]
    try:
        article = Article.objects.get(id=id)
    except :
        return render(request,'404.html',status=404)
    return render(request,'article/detail.html',{'article':article})

# 分页结构，在index界面，搜索界面，分类界面，标签界面等需要分页
# 也就是，需要有一个参数，存储的是index界面或者搜索界面等各界面的文章列表
"""
都是用get方式得到当前页面的页码
如index中，/?page=2
 article/search/?keyword=keyword&page = 2
 article/category/categoryName/?page=2
 article/tag/tagName/?page=2
"""
def paging(request,articles):
    # 将各个分类下的所有文章传进去，然后指出每个页面显示的多少条数据
    paginator = Paginator(articles,1)
    path = clean_path(request)
    page = int(request.GET.get('page',1))
    num_pages = paginator.num_pages
    # AttributeError: 'Page' object has no attribute 'exists'
    page_obj = paginator.get_page(page)
    articles = page_obj.object_list
    return path,page,num_pages,page_obj,articles

def clean_path(request):
    path = str(request.get_full_path())
    if 'page=' in path:
        """
        对数据进行清洗，包括两种情况，第一个是page以？开头，第二个是page以&开头
        字符串索引index(page)返回p的位置，减一得到？或者&的位置，切片去掉
        """
        path = path[:path.index('page=')-1]
        # print(path)
    path += '&' if '/search/' in path else '?'
    return path