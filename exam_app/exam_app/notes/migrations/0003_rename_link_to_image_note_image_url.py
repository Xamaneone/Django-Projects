# Generated by Django 3.2.4 on 2021-06-27 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_image_url_note_link_to_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='link_to_image',
            new_name='image_url',
        ),
    ]