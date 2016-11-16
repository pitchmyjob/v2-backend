# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('ordre', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-ordre', 'name'],
                'verbose_name': "Secteur d'activité",
                'verbose_name_plural': "Liste des secteur d'activité",
            },
        ),
    ]
