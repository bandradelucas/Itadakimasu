# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-24 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado Em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Alterado Em')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.ProductCategory', verbose_name='Pai')),
            ],
            options={
                'verbose_name': 'Categoria de Produto',
                'verbose_name_plural': 'Categorias de Produto',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.ProductCategory', verbose_name='Categoria'),
            preserve_default=False,
        ),
    ]
