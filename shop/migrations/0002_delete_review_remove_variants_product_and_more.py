# Generated by Django 4.2.1 on 2023-06-27 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.RemoveField(
            model_name='variants',
            name='product',
        ),
        migrations.RemoveField(
            model_name='variants',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='variant',
        ),
        migrations.DeleteModel(
            name='Edition',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.DeleteModel(
            name='Variants',
        ),
    ]
