# Generated by Django 3.2.8 on 2022-02-25 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220223_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
    ]