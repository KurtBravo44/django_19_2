# Generated by Django 4.2.7 on 2023-12-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_version_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='current',
            field=models.BooleanField(default=False, verbose_name='признак текущей версии'),
        ),
    ]
