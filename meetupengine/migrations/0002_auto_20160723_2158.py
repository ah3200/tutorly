# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-23 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetupengine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='slug',
            field=models.SlugField(default='classroom-template', max_length=40),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='course-template', max_length=40),
        ),
        migrations.AlterField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='meetupengine.Tutor'),
        ),
    ]
