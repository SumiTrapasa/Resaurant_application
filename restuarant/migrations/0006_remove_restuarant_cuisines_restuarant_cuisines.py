# Generated by Django 4.0.6 on 2022-07-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0005_restuarant_discriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restuarant',
            name='Cuisines',
        ),
        migrations.AddField(
            model_name='restuarant',
            name='Cuisines',
            field=models.ManyToManyField(related_name='restuarants', to='restuarant.cuisines'),
        ),
    ]