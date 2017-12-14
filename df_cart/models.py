from django.db import models
# from df_goods.models import GoodsInfo
from df_user.models import UserInfo


class CartInfo(models.Model):
    """购物车模型类"""

    # 用户和商品之间是多对多的关系，新建购物车模型类来维护
    user = models.ForeignKey('UserInfo')  # 关联用户
    goods = models.ForeignKey('GoodsInfo')  # 关联商品
    count = models.IntegerField()  # 维护商品数量