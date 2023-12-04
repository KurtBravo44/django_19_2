# Generated by Django 4.2.7 on 2023-12-04 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_material_is_published_material_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='materials/'),
        ),
        migrations.AddField(
            model_name='material',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания'),
        ),
    ]
