# Generated by Django 2.2 on 2019-11-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0008_auto_20191111_0645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_title']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='about',
            new_name='about_author',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='category_title',
            field=models.CharField(default=True, help_text='Add category of article', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='facebook',
            field=models.URLField(blank=True, help_text='Add URL of your FB account', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='insta',
            field=models.URLField(blank=True, help_text='Add URL of your insta account', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='linkedin',
            field=models.URLField(blank=True, help_text='Add URL of your linkedin account', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='others',
            field=models.URLField(blank=True, help_text='Add other URL (e.g github account etc)', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(blank=True, help_text='Add URL of your website', max_length=250, null=True),
        ),
    ]
