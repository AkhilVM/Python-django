# Generated by Django 3.2.12 on 2022-02-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_descriptio_place_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='image',
            new_name='img',
        ),
    ]