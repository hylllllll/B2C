from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CartInfo
# from df_user.models import UserInfo
from df_user import user_decorator



@user_decorator.login
def cart(request):
    """购物车"""

    id = request.session['id']  # 获取当前用户id
    carts = CartInfo.objects.filter(user_id=id)  # 获取该id用胡的购物车数据
    # print(carts)

    context = {'page': 1,  # 确定搜索和购物车的样式
               'carts': carts}

    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
def add(request, gid, count):  # 添加的商品的id以及数量
    id = request.session['id']  # 获取用户id
    gid = int(gid)  # 接收商品id
    count = int(count)  # 接收商品数量

    # 获取当前用户浏览的商品的购物车信息
    carts = CartInfo.objects.filter(user_id=id, goods_id=gid)  # Queryset
    if len(carts)>0:  # 判断当前用户是否已添加过该商品
        cart = carts[0]
        cart.count += count  # 如果有（也只会有一个，即第一个）, 加上现在添加的数量
    else:
        cart = CartInfo()
        cart.user_id = id
        cart.goods_id = gid
        cart.count = count
    cart.save()

    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=id).count()  # 得到用户添加了几种商品
        return JsonResponse({'count': count})  # 返回json数据
    else:
        return redirect('/cart/')


@user_decorator.login
def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.count = int(count)
        cart.save()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': count1}
    return JsonResponse(data)


@user_decorator.login
def delete(request, cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok': 1}
    except Exception as e:
        data = {'ok': 0}
    return JsonResponse(data)