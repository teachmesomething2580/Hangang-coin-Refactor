# Generated by Django 2.1.5 on 2019-01-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0002_coinvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinvalue',
            name='is_day_master',
            field=models.BooleanField(default=False),
        ),
    ]