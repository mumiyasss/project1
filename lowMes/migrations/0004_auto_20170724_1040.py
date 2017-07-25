# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import lowMes.models


class Migration(migrations.Migration):

    dependencies = [
        ('lowMes', '0003_message_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=lowMes.models.file_upload),
        ),
    ]