# Generated by Django 4.1.4 on 2023-01-05 08:40

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subscriber', models.EmailField(max_length=128, unique=True, validators=[django.core.validators.EmailValidator()])),
            ],
            options={
                'verbose_name': 'newsletter',
                'verbose_name_plural': 'newsletters',
                'ordering': ['subscriber'],
            },
        ),
        migrations.CreateModel(
            name='ScheduleMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(max_length=3000)),
            ],
            options={
                'verbose_name': 'schedulemail',
                'verbose_name_plural': 'schedulemails',
                'ordering': ['-created'],
            },
        ),
    ]
