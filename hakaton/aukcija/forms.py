from django import forms
from .models import Korisnik, OblastiInteresovanja, KorisnickeOblastiInteresovanja
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class FormaKorisnik (forms.ModelForm):
	class Meta:
		model = Korisnik
		fields = '__all__'

class FormaOblastiInteresovanja (forms.ModelForm):
	class Meta:
		model = OblastiInteresovanja
		fields = '__all__'

class FormaKorisnickeOblastiInteresovanja (forms.ModelForm):
	class Meta:
		model = KorisnickeOblastiInteresovanja
		fields = '__all__'

class FormaRegistracija(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

