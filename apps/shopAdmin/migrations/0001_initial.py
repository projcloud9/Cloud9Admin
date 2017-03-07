# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 09:34
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CnShop',
            fields=[
                ('shop_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='店铺Id')),
                ('shop_name', models.CharField(max_length=10, verbose_name='店铺名称')),
                ('sells_type', models.CharField(max_length=10, verbose_name='商品类型')),
                ('legal_name', models.CharField(max_length=10, verbose_name='法人姓名')),
                ('legal_id', models.CharField(max_length=20, verbose_name='法人身份证号码')),
                ('address', models.CharField(max_length=100, verbose_name='法人联系地址')),
                ('avatar', models.ImageField(default='media/avatar/default_shop.png', upload_to='media/avatar')),
                ('rank', models.CharField(default='一星卖家', max_length=10, verbose_name='会员等级')),
                ('shop_ave_score', models.CharField(default=0, max_length=5, verbose_name='店铺打分')),
                ('service_score', models.CharField(default=0, max_length=5, verbose_name='服务打分')),
                ('logistics_score', models.CharField(default=0, max_length=5, verbose_name='物流打分')),
                ('is_active', models.BooleanField(default=False, verbose_name='店铺状态')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='店铺创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='店主id')),
            ],
            options={
                'verbose_name': '店铺信息',
                'verbose_name_plural': '店铺信息',
            },
        ),
    ]