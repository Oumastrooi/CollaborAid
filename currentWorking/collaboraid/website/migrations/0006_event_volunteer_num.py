# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-02 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20161202_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='volunteer_num',
            field=models.IntegerField(default=1),
        ),
    ]
