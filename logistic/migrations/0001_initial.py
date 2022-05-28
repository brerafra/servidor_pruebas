# Generated by Django 4.0.4 on 2022-05-27 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, unique=True)),
                ('distance', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fuel_consumption', models.PositiveIntegerField()),
                ('distance_traveled', models.BigIntegerField(default=0)),
                ('fuel_consumed', models.BigIntegerField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistic.city')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'db_table': 'Vehicle',
                'ordering': ['vehicle_id'],
            },
        ),
    ]