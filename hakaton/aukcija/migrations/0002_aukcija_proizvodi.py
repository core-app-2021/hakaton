# Generated by Django 3.1.5 on 2021-04-24 13:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aukcija', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proizvodi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=100)),
                ('slika', models.FileField(upload_to='')),
                ('opsi', models.TextField()),
                ('cijena', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('korisnikID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aukcija.korisnik')),
            ],
        ),
        migrations.CreateModel(
            name='Aukcija',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datum', models.DateField(default=datetime.date.today)),
                ('vrijeme_pocetka', models.TimeField(default=django.utils.timezone.now)),
                ('vrijeme_trajanja', models.TimeField(default=datetime.time(2, 0))),
                ('oblastinteresovanjaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aukcija.oblastiinteresovanja')),
                ('proizvodID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aukcija.proizvodi')),
            ],
        ),
    ]
