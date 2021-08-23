from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, models
from django.views import View

from .forms import *

class Register(View):
    pass

class Login(View):
    def get(self,request,*args,**kwargs):
        # 在get方式中，表单的格式默认是有效的，post的方式中，只有提交后进行判断，才能进行表单的判定
        form_is_valid = True

        # 只能使用global关键字进行全局变量的传递，给get方式前的url储存起来，给post后的使用
        global prevous_url
        prevous_url = request.META.get('HTTP_REFERER','/')
        print('revous_url = %s'%prevous_url)
        form = UserLoginForm()
        context = {'from':form,'form_is_valid':form_is_valid}
        return render(request,'user/user.html',context)

    def post(self,request,*args,**kwargs):
        # print('prevous_url = %s'%prevous_url)
        user_login_form = UserLoginForm(data=request.POST)
        # print(user_login_form)
        """
        如果表单所填的内容符合规则，cleaned_data清洗出有用的数据，根据表单类中定义所需的字段
        此时并不是用户的判断，而是表单的内容是否符合字段的规则
        """
        form_is_valid = user_login_form.is_valid()
        # 如果表单的内容符合规则
        if form_is_valid:
            data = user_login_form.cleaned_data
            # print(data)
            """
            根据清理出来的必须字段，进行校验
            进行数据库的检验，判断用户是否存在，如果存在返回表的对象，也就是用户对象，如果不存在那么为None
            """
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request,user)
                # print('prevous_url = %s'%prevous_url)
                # 通过get方法前得到的previous_url
                return redirect(prevous_url)
        # 如果表单的内容不符合规则，那么
        else:
            context = {'form_is_valid':form_is_valid}
            return render(request,'user/user.html',context)

def dropdown(request):
    logout(request)
    referer = request.META.get('HTTP_REFERER', '/')
    # print('referer=%s' % referer)
    # print('path=%s'%request.get_full_path())
    return redirect(referer)


def forgot(request):
    return None


