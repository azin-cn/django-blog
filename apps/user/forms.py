#coding=utf-8
from django import forms

class UserLoginForm(forms.Form):
    # 用户登陆中，必须要的字段是用户名和密码
    # 使用表单类的方法是直接生成表单类对象，然后得到清洗的数据，使用is_valid判断是否有效
    username = forms.CharField()
    password = forms.CharField()