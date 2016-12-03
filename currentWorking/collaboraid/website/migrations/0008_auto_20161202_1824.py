# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20161202_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('venue', models.CharField(blank=True, max_length=128)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=30)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='event_images')),
                ('description', models.TextField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_owner',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
