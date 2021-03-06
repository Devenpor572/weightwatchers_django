# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mass', models.PositiveIntegerField()),
                ('calories', models.PositiveIntegerField()),
                ('saturated_fat', models.PositiveIntegerField()),
                ('sugar', models.PositiveIntegerField()),
                ('protein', models.PositiveIntegerField()),
                ('is_exempt', models.BooleanField()),
            ],
        ),
    ]
