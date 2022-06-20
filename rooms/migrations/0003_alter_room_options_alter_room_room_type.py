# Generated by Django 4.0.5 on 2022-06-19 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['room_number'], 'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='rooms.roomtype', verbose_name='Room Type'),
        ),
    ]
