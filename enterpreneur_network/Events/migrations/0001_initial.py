# Generated by Django 2.2 on 2019-11-12 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(help_text='Add category of event', max_length=100)),
            ],
            options={
                'ordering': ['category_title'],
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Organizer Name')),
                ('phone', models.CharField(max_length=20, verbose_name='Contact Phone')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Organizer Email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Web Address')),
                ('organizer_picture', models.ImageField(help_text='Add image of organizer', upload_to='')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=12, verbose_name='Zip/Post Code')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateField(default=django.utils.timezone.now, verbose_name='Day of Event')),
                ('starting_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Starting Time')),
                ('end_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Ending Time')),
                ('picture', models.ImageField(help_text='Add picture related to event', upload_to='')),
                ('description', models.TextField(verbose_name='Event Description')),
                ('featured', models.BooleanField(default=False)),
                ('cost', models.IntegerField(help_text='Add cost of event in case of free, write 0')),
                ('label', models.CharField(choices=[('o', 'On Time'), ('d', 'Delayed'), ('c', 'Completed')], default='o', help_text='Choose Event Status from here', max_length=1)),
                ('attendees', models.ManyToManyField(blank=True, to='Events.RegisteredUser')),
                ('categories', models.ManyToManyField(to='Events.Category')),
                ('event_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.Organizer')),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Events.Venue')),
            ],
            options={
                'ordering': ['-event_date'],
            },
        ),
    ]
