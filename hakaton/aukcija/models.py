from django.db import models
from django.utils import timezone
import datetime

class Korisnik (models.Model):
	id = models.AutoField(primary_key=True)
	# korisnickoime = models.CharField(max_length=20)
	naziv = models.CharField(max_length=200)
	adresa = models.CharField(max_length=200)
	jib = models.CharField(max_length=13)
	pib =  models.CharField(max_length=12)
	email = models.EmailField()
	# user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default=True)

	def __str__ (self):
		return self.naziv

class OblastiInteresovanja (models.Model):
	id = models.AutoField(primary_key=True)
	naziv = models.CharField(max_length=200)

	def __str__ (self):
		return self.naziv

class KorisnickeOblastiInteresovanja(models.Model):
	id = models.AutoField(primary_key=True)
	korisnikID = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
	oblastiinteresovanjaID = models.ForeignKey(OblastiInteresovanja, on_delete=models.CASCADE)

class Proizvodi(models.Model):
	id = models.AutoField(primary_key=True)
	naziv = models.CharField(max_length=100)
	slika = models.FileField()
	opsi = models.TextField()
	cijena = models.DecimalField(max_digits=8, decimal_places=2, default= 0.00)
	korisnikID = models.ForeignKey(Korisnik, on_delete=models.CASCADE)

class Aukcija (models.Model):
	id = models.AutoField(primary_key=True)
	proizvodID = models.ForeignKey(Proizvodi, on_delete=models.CASCADE)
	datum = models.DateField(default = datetime.date.today)
	vrijeme_pocetka = models.TimeField(default= timezone.now)
	vrijeme_trajanja = models.TimeField(default = datetime.time(2, 00))
	oblastinteresovanjaID = models.ForeignKey(OblastiInteresovanja, on_delete=models.CASCADE) 