# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-01 23:20


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='post_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
