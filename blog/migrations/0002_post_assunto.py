# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='assunto',
            field=models.TextField(default='desconhecido'),
        ),
    ]
