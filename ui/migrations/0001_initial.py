# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('icon', models.CharField(blank=True, max_length=1000, null=True)),
                ('img', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=1000, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('modify_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
        ),
    ]
