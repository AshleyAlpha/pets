# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petsanimals', '0002_remove_client_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='first_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='last_name',
            new_name='Last_name',
        ),
    ]
