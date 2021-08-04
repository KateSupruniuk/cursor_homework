# Generated by Django 3.2.5 on 2021-08-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('gasoline', 'Gasoline')], default='petrol', max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Fuel Type',
                'verbose_name_plural': 'Fuel Types',
            },
        ),
        migrations.RemoveField(
            model_name='car',
            name='fuel_type',
        ),
        migrations.AlterField(
            model_name='car',
            name='capacity',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=3, default=30000, max_digits=12),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.CharField(choices=[('passenger', 'Passenger'), ('truck', 'Truck'), ('special', 'Special')], default='passenger', max_length=20),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.fueltype'),
            preserve_default=False,
        ),
    ]
