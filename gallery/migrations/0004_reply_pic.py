# Generated by Django 3.2.8 on 2021-11-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20211102_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]