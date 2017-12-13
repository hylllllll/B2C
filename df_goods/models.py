from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')  # 上传商品图片，存储路径
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    is_delete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20, default='500g')  # 单位
    gclick = models.IntegerField()  # 点击量--人气
    gabstract = models.CharField(max_length=200)  # 价格页面的简介
    gnum = models.IntegerField()  # 库存
    gdetail = HTMLField()
    gtype = models.ForeignKey(TypeInfo)

    # gad = models.BooleanField(default=False) # 推荐

    def __str__(self):
        return self.gtitle
