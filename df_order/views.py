from django.shortcuts import render, redirect
from df_user import user_decorator
from django.db import transaction
from df_cart.models import CartInfo
from df_user.models import UserInfo


@user_decorator.login
def order(request):
    """"""

    id = request.session['id']
    user = UserInfo.objects.get(pk=id)
    cartid = request.GET.getlist('cart_id')

    carts = []
    totals = 0  # 总计
    try:
        for id in cartid:
            goods_info = CartInfo.objects.get(id=id).goods
            cart = CartInfo.objects.get(id=id)
            total = goods_info.gprice * cart.count  # 小计
            carts.append([cart, total])
            totals += total
            context = {'carts': carts,
                       'totals': totals}
            rec = render(request, 'df_order/place_order.html', context)
    except:
        rec = redirect('/cart/')

    return rec


@transaction.atomic()
@user_decorator.login
def order_handle(request):
    """
    用事物来完成：一旦有操作失败，全部回退
    1、创建订单对象
    2、判断商品库存
    3、创建详单对象
    4、修改商品库存
    5、删除购物车信息
    """

    tran_id = transaction.savepoint()
    pass
