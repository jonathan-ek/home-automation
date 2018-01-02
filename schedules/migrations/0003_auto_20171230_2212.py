# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-30 21:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20160730_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='device',
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='friday',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='monday',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='saturday',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='sunday',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='thursday',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='tuesday',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='wednesday',
            field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(
            model_name='scheduleslot',
            name='end',
        ),
        migrations.RemoveField(
            model_name='scheduleslot',
            name='start',
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='end',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(-23.99), django.core.validators.MaxValueValidator(23.99)]),
        ),
        migrations.AddField(
            model_name='scheduleslot',
            name='start',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(-23.99), django.core.validators.MaxValueValidator(23.99)]),
        ),
    ]
