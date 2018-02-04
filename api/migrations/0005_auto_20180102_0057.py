# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-01 23:57


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_button_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='button',
            name='manually_active',
            field=models.BooleanField(default=False),
        ),
    ]
