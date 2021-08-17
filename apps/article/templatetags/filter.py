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
    print('index=',index,"  ",'current=',current)
    if index <= current-2:
        return True
    elif index-2>=current:
        return True
    else:
        return False
