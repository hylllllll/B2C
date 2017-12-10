from django.shortcuts import render


def register(request):
    """注册"""
    return render(request, 'df_user/register.html')
