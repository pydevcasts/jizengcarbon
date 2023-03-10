# Generated by Django 4.1.4 on 2022-12-29 22:57

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'slider', 'verbose_name_plural': 'sliders'},
        ),
        migrations.AddField(
            model_name='slider',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='slider/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slug',
            field=models.CharField(max_length=128, unique_for_month='published_at'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='slider',
            name='summary',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(help_text='The text mus be unique', max_length=128, unique_for_month='published_at'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
