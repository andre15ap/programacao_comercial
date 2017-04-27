# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 03:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plataforma', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('plataforma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plataforma.plataforma')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
