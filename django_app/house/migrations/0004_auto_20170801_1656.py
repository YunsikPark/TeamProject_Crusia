# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_house_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='amenities',
            field=models.CharField(choices=[('House', '집전체'), ('Individual', '개인실'), ('Shared_Room', '다인실')], max_length=500),
        ),
    ]
