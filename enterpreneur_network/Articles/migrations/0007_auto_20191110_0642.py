# Generated by Django 2.2 on 2019-11-10 14:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0006_auto_20191110_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
