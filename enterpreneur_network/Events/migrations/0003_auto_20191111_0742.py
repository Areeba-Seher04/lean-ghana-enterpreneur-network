# Generated by Django 2.2 on 2019-11-11 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20191111_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='YYYY-MM-D', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Event Date'),
        ),
    ]