# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 05:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_text_rich'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text_rich',
        ),
    ]
