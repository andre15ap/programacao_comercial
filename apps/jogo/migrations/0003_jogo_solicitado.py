# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0002_auto_20170426_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='solicitado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]