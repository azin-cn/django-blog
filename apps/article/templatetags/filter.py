#coding=utf-8
import random
from django import template
register = template.Library()

# 定义一个除法，求阅读时长的分数
@register.filter
def length(content):
    content = content.replace('&nbsp;', '').replace('\t', '').replace('\n','')
    return len(content)//1

@register.filter
def spendTime(length):
    return length//300+1

# 使用simple_tag标注的函数可以直接调用
@register.simple_tag
def color():
    # randint(a,b)包含a,b
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    color = 'rgb(%s,%s,%s)'%(red,green,blue)
    return color

# 需要在ifelse中判断，只能用filter
@register.filter
def compare(index,current):
    # print('index=',index,"  ",'current=',current)
    if index <= current-2:
        return True
    elif index-2>=current:
        return True
    else:
        return False

# 解决多参数的get请求参数消失问题，以及对路径进行清洗
@register.filter
def clean_path(full_path):
    path = str(full_path)
    if 'page=' in path:
        """
        对数据进行清洗，包括两种情况，第一个是page以？开头，第二个是page以&开头
        字符串索引index(page)返回p的位置，减一得到？或者&的位置，切片去掉
        """
        path = path[:path.index('page=')-1]
        print(path)
    path += '&' if '/search/' in path else '?'
    # print(path)
    return path