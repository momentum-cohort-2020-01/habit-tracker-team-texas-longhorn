# Generated by Django 3.0.4 on 2020-03-08 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0010_merge_20200308_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
