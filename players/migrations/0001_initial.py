# Generated by Django 2.2.7 on 2019-11-09 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 55, 47, 501739))),
                ('email', models.CharField(max_length=64)),
                ('xp', models.IntegerField()),
                ('coin', models.IntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=64, null=True)),
                ('playing', models.IntegerField(default=1)),
                ('country', models.CharField(max_length=15)),
            ],
        ),
    ]