# Generated by Django 4.1.4 on 2022-12-30 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('category', '0002_alter_category_options_alter_category_banner_and_more'),
        ('product', '0002_rename_banner_product_banner_1_product_banner_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='category.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='tag.tag'),
        ),
    ]
