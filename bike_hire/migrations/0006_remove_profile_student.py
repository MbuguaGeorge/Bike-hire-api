# Generated by Django 3.2 on 2021-05-08 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bike_hire', '0005_auto_20210505_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='student',
        ),
    ]
