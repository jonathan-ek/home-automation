# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 00:04


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wired', '0005_auto_20180102_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='hide_schedule',
            field=models.BooleanField(default=False),
        ),
    ]
