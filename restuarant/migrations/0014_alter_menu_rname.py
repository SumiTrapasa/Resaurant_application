# Generated by Django 4.0.6 on 2022-07-07 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0013_alter_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='rname',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='restuarant.restuarant'),
        ),
    ]
