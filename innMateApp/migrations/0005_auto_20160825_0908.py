# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-25 09:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('innMateApp', '0004_auto_20160825_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('cell', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('cell', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('cell', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='establishment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='innMateApp.Establishment'),
        ),
        migrations.AddField(
            model_name='contractor',
            name='establishment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='innMateApp.Establishment'),
        ),
        migrations.AddField(
            model_name='guest',
            name='establishment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='innMateApp.Establishment'),
        ),
    ]
