# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octopus', '0002_auto_20180510_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hypothesis',
            options={'verbose_name_plural': 'hypothesis'},
        ),
        migrations.AddField(
            model_name='hypothesis',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hypothesis',
            name='text',
            field=models.TextField(),
        ),
    ]