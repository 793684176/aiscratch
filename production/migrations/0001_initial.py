# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-08-12 12:50
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='姓名')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='邮箱')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Productions',
            fields=[
                ('puuid', models.UUIDField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50, verbose_name='作品名称')),
                ('sb3file', models.FileField(blank=True, null=True, upload_to='sb3file/')),
                ('sb3snap', models.FileField(blank=True, null=True, upload_to='sb3snap/')),
                ('category', models.CharField(blank=True, max_length=100, null=True, verbose_name='作品类别')),
                ('describe', models.TextField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('is_public', models.BooleanField(default='False', verbose_name='是否公开')),
                ('is_previewable', models.BooleanField(default='False', verbose_name='是否可预览')),
                ('is_editable', models.BooleanField(default='False', verbose_name='是否可编辑')),
                ('is_shareable', models.BooleanField(default='False', verbose_name='是否可分享')),
                ('is_downloadable', models.BooleanField(default='False', verbose_name='是否可下载')),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '作品信息',
                'verbose_name_plural': '作品信息',
            },
        ),
    ]
