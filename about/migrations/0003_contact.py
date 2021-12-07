# Generated by Django 3.1.3 on 2021-12-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20211205_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=254)),
                ('subheader', models.TextField(max_length=254)),
                ('telephone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('instagram_handle', models.TextField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Contact Section',
            },
        ),
    ]
