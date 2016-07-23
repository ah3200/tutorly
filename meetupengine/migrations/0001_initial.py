# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 23:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=50)),
                ('datetime_from', models.DateTimeField()),
                ('datetime_to', models.DateTimeField()),
                ('schedule', models.TextField()),
                ('max_registration', models.IntegerField()),
                ('registered', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('subject', models.TextField(max_length=50)),
                ('level', models.TextField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_status', models.TextField(max_length=20)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetupengine.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='')),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40)),
                ('website', models.URLField(blank=True, default='')),
                ('bio', models.TextField(blank=True, default='')),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetupengine.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetupengine.Tutor'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetupengine.Course'),
        ),
    ]