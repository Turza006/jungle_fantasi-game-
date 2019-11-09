# Generated by Django 2.2.7 on 2019-11-09 14:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 55, 47, 555739))),
                ('percentage', models.IntegerField()),
                ('level', models.IntegerField()),
                ('expair', models.DateTimeField(blank=True, null=True)),
                ('_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Players')),
            ],
        ),
    ]
