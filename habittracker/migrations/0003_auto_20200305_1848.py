# Generated by Django 3.0.4 on 2020-03-05 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0002_auto_20200305_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='record',
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
