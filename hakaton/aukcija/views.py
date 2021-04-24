from django.shortcuts import render,redirect
from .forms import FormaKorisnik, FormaRegistracija, FormaOblastiInteresovanja, FormaKorisnickeOblastiInteresovanja
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index (request):
	return render (request, 'index.html')

def uizradi (request):
	return render (request, 'uizradi.html')

def registracija(request):
	form = FormaRegistracija()
	if request.method == 'POST':
		form = FormaRegistracija(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			# group = Group.objects.get(name='Korisnik')
			# user.groups.add(group)

			messages.success(request, 'Nalog za ' + username + ' je uspjesno kreiran')
			return redirect('prijava')
	sadrzaj = {'form': form}
	return render(request, 'registracija.html', sadrzaj)

def prijava(request):
	if request.method == 'POST':
		korisnickoime = request.POST.get('korisnickoime')
		lozinka = request.POST.get('lozinka')

		korisnik = authenticate(request, username=korisnickoime, password=lozinka)

		if korisnik is not None:
			login (request, korisnik) 
			return redirect('base') 
		else:
			messages.info(request, 'Ime ili lozinka su netecni!')
	sadrzaj = {}
	return render(request, 'prijava.html', sadrzaj)

def odjava(request):
	logout(request)
	return redirect('index')

#forme za unos

def unos_korisnika (request):
	form = FormaKorisnik(request.POST or None)
	if form.is_valid():
		form.save()
		form = FormaKorisnik()
		return redirect('index')
	sadrzaj = {
		"form": form
	}
	return render(request, "unos_korisnika.html", sadrzaj)

def oblast_interesovanja (request):
	form = FormaOblastiInteresovanja(request.POST or None)
	if form.is_valid():
		form.save()
		form = FormaOblastiInteresovanja()
		return redirect('index')
	sadrzaj = {
		"form": form
	}
	return render(request, "oblastinteresovanja_unos.html", sadrzaj)

def korisnicke_oblasti_interesovanja (request):
	form = FormaKorisnickeOblastiInteresovanja(request.POST or None)
	if form.is_valid():
		form.save()
		form = FormaKorisnickeOblastiInteresovanja()
		return redirect('index')
	sadrzaj = {
		"form": form
	}
	return render(request, "korisnicke_oblasti_interesovanja_unos.html", sadrzaj)



#prikazi podataka

def base (request):
	return render (request, 'base.html')