# Generated by Django 2.2 on 2019-11-11 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0018_auto_20191111_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_title']},
        ),
        migrations.AlterModelOptions(
            name='organizer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='registereduser',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ['name']},
        ),
    ]