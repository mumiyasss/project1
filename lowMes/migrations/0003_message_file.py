# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-23 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowMes', '0002_chat_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='lowMes/messages/files'),
        ),
    ]