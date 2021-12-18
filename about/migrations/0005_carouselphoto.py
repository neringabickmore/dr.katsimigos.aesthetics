# Generated by Django 3.1.3 on 2021-12-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20211207_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('friendly_title', models.CharField(max_length=200, verbose_name='Friendly Title')),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'verbose_name_plural': 'Carousel Photos',
            },
        ),
    ]