# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]