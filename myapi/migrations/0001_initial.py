# Generated by Django 4.1.7 on 2023-03-24 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('cast', models.CharField(max_length=20)),
                ('duration', models.TimeField(default=0)),
                ('type', models.CharField(max_length=20)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('reviews', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
