from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('uizradi', views.uizradi, name='uizradi'),
	path('base', views.base, name='base'),
	path('registracija', views.registracija, name='registracija'),
	path('prijava', views.prijava, name='prijava'),
	path('odjava', views.odjava, name='odjava'),

	#forme za unos

	path('unos-korisnika', views.unos_korisnika, name='unos-korisnika'),
	path('unos-oblastinteresovanja', views.oblast_interesovanja, name='unos-oblastinteresovanja'),
	path('unos-korisnickeoblastinteresovanja', views.korisnicke_oblasti_interesovanja, name='unos-korisnickeoblastinteresovanja'),
]