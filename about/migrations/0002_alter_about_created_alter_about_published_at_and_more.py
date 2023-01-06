# Generated by Django 4.1.4 on 2022-12-29 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='about',
            name='slug',
            field=models.CharField(max_length=128, unique_for_month='published_at'),
        ),
        migrations.AlterField(
            model_name='about',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(help_text='The text mus be unique', max_length=128, unique_for_month='published_at'),
        ),
        migrations.AlterField(
            model_name='about',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]