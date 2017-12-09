from django.db import models


class UserInfo(models.Model):
    """用户"""

    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=20)
    uaddr = models.CharField(max_length=100)
    upost = models.CharField(max_length=6)
