# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 17:37


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
