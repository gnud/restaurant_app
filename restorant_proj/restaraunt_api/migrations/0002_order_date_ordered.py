# Generated by Django 3.0.9 on 2020-08-04 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaraunt_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_ordered'),
        ),
    ]
