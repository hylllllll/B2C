from django.http import HttpResponseRedirect


#  利用session判断用户是否已登录的装饰器
def login(func):
    def login_func(request, *args, **kwargs):

        # 判断是否存在之前存过用户id--session['id']
        if 'id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_func
