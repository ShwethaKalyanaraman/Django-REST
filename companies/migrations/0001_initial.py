# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-26 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('highest', models.FloatField()),
                ('lowest', models.FloatField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
