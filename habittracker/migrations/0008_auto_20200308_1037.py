# Generated by Django 3.0.4 on 2020-03-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0007_auto_20200306_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]