# Generated by Django 3.2.8 on 2023-10-09 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20231009_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price1',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='year1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='year2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='year3',
        ),
    ]
