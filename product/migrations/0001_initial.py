# Generated by Django 4.1.4 on 2022-12-29 13:24

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_alter_category_options_alter_category_banner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(help_text='The text mus be unique', max_length=128, unique_for_month='published_at')),
                ('slug', models.CharField(max_length=128, unique_for_month='published_at')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('summary', models.CharField(max_length=128)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d')),
                ('views', models.IntegerField(default=0)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='category.category', verbose_name='دسته بندی')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='tag.tag', verbose_name='برچسب')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['-published_at'],
                'get_latest_by': ['-published_at'],
            },
        ),
    ]
