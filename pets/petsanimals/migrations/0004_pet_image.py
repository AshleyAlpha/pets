# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsanimals', '0003_auto_20190417_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(null=True, upload_to='viva/'),
        ),
    ]
