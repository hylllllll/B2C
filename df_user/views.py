from django.shortcuts import render, redirect
from hashlib import sha1
from .models import UserInfo
from django.http import HttpResponse, HttpResponseRedirect

def register(request):
    """注册"""
    return render(request, 'df_user/register.html')


def register_handle(request):
    """注册信息"""
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码是否一致
    if upwd!=upwd2:
        # 密码不一致，重定向到注册页
        return redirect('user/register/')
    else:
        # 加密密码
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        upwd3 = s1.hexdigest()
        # 创建模型对象,添加数据
        user = UserInfo()
        user.uname = uname
        user.upwd = upwd3
        user.uemail = uemail
        # 一定要保存
        user.save()# 封装了commit等操作
        # 密码一致，重定向到登录页面
        return redirect('/user/login/')


def login(request):
    uname = request.COOKIES.get('uname', '')# 默认为空
    context = {'uname': uname, 'error_uname': 0, 'error_upwd': 0}
    return render(request, 'df_user/login.html', context)


def user_handel(request):
    # 接收表单数据
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    ename = post.get('error_uname')
    epwd = post.get('error_upwd')
    remember = post.get('remember', '')

    # 筛选出用户名为uname的用户数据
    user = UserInfo.objects.filter(uname=uname)
    # print(user)
    if len(user):
        # 查询到的用户数据个数不为空,说明有这个用户,下面匹配密码,密码是sha1加密的
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        s2 = s1.hexdigest()
        # 判断密码是否相等
        if s2==user[0].upwd:
            red = HttpResponseRedirect('/user/info')
            # 判断是否选中记住用户名,选中为'1',默认为''
            if remember:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['uname'] = uname
            request.session['id'] = user[0].id
            return red
        else:
            context = {'error_uname': 0, 'error_upwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'error_name': 1, 'error_upwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)