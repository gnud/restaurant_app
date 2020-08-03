# Generated by Django 3.0.9 on 2020-08-03 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='restaraunt_api.Company'
                    )
                 ),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('menu', models.ManyToManyField(to='restaraunt_api.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='restaraunt_api.Company'
                )),
                ('products', models.ManyToManyField(to='restaraunt_api.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
