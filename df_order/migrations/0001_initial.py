# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_user', '0002_auto_20171210_1531'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('odate', models.DateTimeField(auto_now=True)),
                ('opay', models.BooleanField(default=False)),
                ('ototal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('oaddr', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_order.OrderInfo'),
        ),
    ]
