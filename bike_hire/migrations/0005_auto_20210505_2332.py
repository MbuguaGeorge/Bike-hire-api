# Generated by Django 3.2 on 2021-05-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_hire', '0004_auto_20210429_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]