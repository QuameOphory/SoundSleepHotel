# Generated by Django 4.0.5 on 2022-06-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='roomtype_code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Room Type Code'),
        ),
    ]