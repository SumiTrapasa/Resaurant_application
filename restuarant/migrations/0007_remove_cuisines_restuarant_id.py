# Generated by Django 4.0.6 on 2022-07-05 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0006_remove_restuarant_cuisines_restuarant_cuisines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuisines',
            name='restuarant_id',
        ),
    ]