# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 00:05
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]