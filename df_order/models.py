from django.db import models
from df_user.models import UserInfo
from df_goods.models import GoodsInfo


class OrderInfo(models.Model):
    """订单模型类，编号、用户id、时间、支付状态、总金额、收货地址"""

    oid = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey(UserInfo)
    odate = models.DateTimeField(auto_now=True)
    opay = models.BooleanField(default=False)
    ototal = models.DecimalField(max_digits=6, decimal_places=2)  # 这个值可以算出来，但是为了减少服务器压力，存在数据库中
    oaddr = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    """订单详情，每个商品id、所属订单id，商品价格、商品数量"""

    goods = models.ForeignKey(GoodsInfo)
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()