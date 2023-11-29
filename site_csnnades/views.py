from django.shortcuts import render, redirect
from .forms import GranadaForm
from .models import Granada


def cadastrar_granada(request, mapa_slug):
    if request.method == 'POST':
        form = GranadaForm(request.POST)
        if form.is_valid():
            granada = form.save(commit=False)
            granada.nome_mapa = mapa_slug
            granada.save()
            return redirect('home')
    else:
        form = GranadaForm()

    return render(request, 'cadastro_granada.html', {'form': form, 'mapa_slug': mapa_slug})

def home(request):
    return render(request, 'home.html')

def mirage(request):
    granadas = Granada.objects.filter(nome_mapa='Mirage')
    return render(request, 'mirage.html', {'granadas': granadas})

def inferno(request):
    granadas = Granada.objects.filter(nome_mapa='Inferno')
    return render(request, 'inferno.html', {'granadas': granadas})

def overpass(request):
    granadas = Granada.objects.filter(nome_mapa='Overpass')
    return render(request, 'overpass.html', {'granadas': granadas})

def vertigo(request):
    granadas = Granada.objects.filter(nome_mapa='Vertigo')
    return render(request, 'vertigo.html', {'granadas': granadas})

def anubis(request):
    granadas = Granada.objects.filter(nome_mapa='Anubis')
    return render(request, 'anubis.html', {'granadas': granadas})

def nuke(request):
    granadas = Granada.objects.filter(nome_mapa='Nuke')
    return render(request, 'nuke.html', {'granadas': granadas})

def ancient(request):
    granadas = Granada.objects.filter(nome_mapa='Ancient')
    return render(request, 'ancient.html', {'granadas': granadas})
