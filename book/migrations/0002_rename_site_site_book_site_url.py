# Generated by Django 3.2.8 on 2021-10-29 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='site_site',
            new_name='site_url',
        ),
    ]