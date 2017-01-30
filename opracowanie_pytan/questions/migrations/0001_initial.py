# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kierunek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Odpowiedz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=2048, null=True)),
                ('author', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Pytanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('order', models.IntegerField()),
                ('reserved', models.CharField(blank=True, max_length=64, null=True)),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Kierunek')),
            ],
        ),
        migrations.AddField(
            model_name='odpowiedz',
            name='quesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Pytanie'),
        ),
    ]
