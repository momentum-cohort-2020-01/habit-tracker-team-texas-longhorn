# Generated by Django 3.0.4 on 2020-03-06 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0005_auto_20200305_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='name',
        ),
    ]
