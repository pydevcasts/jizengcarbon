# Generated by Django 4.1.4 on 2022-12-30 11:44

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import painless.models.validations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'member', 'verbose_name_plural': 'members'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'team', 'verbose_name_plural': 'teams'},
        ),
        migrations.AlterField(
            model_name='member',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='memnber/%Y/%m/%d', validators=[painless.models.validations.validate_file_extension, painless.models.validations.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='member',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='whatsapp',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='team',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='team',
            name='summary',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='team',
            name='title',
            field=models.CharField(help_text='The text mus be unique', max_length=128, unique_for_month='published_at'),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
