# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pytanie',
            name='order',
        ),
    ]
