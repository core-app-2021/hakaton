# Generated by Django 3.1.5 on 2021-04-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aukcija', '0004_korisnik_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='korisnik',
            name='user',
        ),
    ]