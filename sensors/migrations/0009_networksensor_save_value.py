# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 14:46


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0008_networksensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='networksensor',
            name='save_value',
            field=models.BooleanField(default=False),
        ),
    ]