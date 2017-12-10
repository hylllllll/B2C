from django.shortcuts import render, redirect
from hashlib import sha1
from .models import UserInfo


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
        # 密码一致，重定向到登录页面
        return redirect('/user/login/')
