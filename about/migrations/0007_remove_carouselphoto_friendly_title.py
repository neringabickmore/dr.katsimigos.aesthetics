# Generated by Django 3.1.3 on 2021-12-08 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20211208_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselphoto',
            name='friendly_title',
        ),
    ]
