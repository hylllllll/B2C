from django.shortcuts import render


# 注册
def register(request):
    return render(request, 'df_user/register.html')
