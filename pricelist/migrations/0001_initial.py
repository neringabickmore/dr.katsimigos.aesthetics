# Generated by Django 3.2.8 on 2021-12-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricelistIntro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=10000)),
            ],
            options={
                'verbose_name_plural': 'Pricelist Section',
            },
        ),
    ]