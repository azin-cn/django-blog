from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from extra_apps.DjangoUeditor.models import UEditorField

"""
对导航栏进行注册，通过数据库的方式进行更新
同时也可以通过定义全局变量的方式进行数据的添加删除

"""
class Navigation(models.Model):
    id = models.AutoField(primary_key=True)
    nav = models.CharField(max_length=4,unique=True,verbose_name='导航栏目')
    url = models.CharField(max_length=64,default='#' ,verbose_name='导航路径')
    class Meta:
        ordering = ('id',)
        verbose_name = '导航'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    tag = models.CharField(max_length=12,unique=True,verbose_name='标签')
    created = models.DateTimeField(verbose_name='创建时间',default=timezone.now)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.tag

class Category(models.Model):
    category = models.CharField(max_length=12,verbose_name='类别',unique=True)
    created = models.DateTimeField(verbose_name='创建时间',default=timezone.now)
    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.category

class Article(models.Model):
    author = models.ForeignKey(User, verbose_name='作者',
                                   default='admin', on_delete=models.SET_DEFAULT,null=True)
    title = models.CharField(verbose_name='标题', max_length=32)
    content = RichTextUploadingField(verbose_name='内容',default='正文：')
    # 没有设置其为非必填字段，这里就会导致必须勾选了所有选项之后才让保存，需要设置blank=True，非必填项
    tag = models.ManyToManyField(Tag, verbose_name='标签',blank=True)
    category = models.ForeignKey(Category, verbose_name='类别',
                                 default='default', on_delete=models.SET_DEFAULT,null=True)
    count = models.PositiveIntegerField(default=0,verbose_name='浏览量')
    # 参数 default = timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    # 除了字段信息外，可以给表定义一些元数据，对整张表起作用
    # 对表格数据进行排序，按照元组元素的顺序进行排序
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title
