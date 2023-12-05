from django.shortcuts import render, redirect
from .forms import GranadaForm
from .models import Granada
from django.contrib.auth.decorators import login_required


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

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def mirage(request):
    granadas = Granada.objects.filter(nome_mapa='Mirage')
    return render(request, 'mirage.html', {'granadas': granadas})

@login_required
def inferno(request):
    granadas = Granada.objects.filter(nome_mapa='Inferno')
    return render(request, 'inferno.html', {'granadas': granadas})

@login_required
def overpass(request):
    granadas = Granada.objects.filter(nome_mapa='Overpass')
    return render(request, 'overpass.html', {'granadas': granadas})

@login_required
def vertigo(request):
    granadas = Granada.objects.filter(nome_mapa='Vertigo')
    return render(request, 'vertigo.html', {'granadas': granadas})

@login_required
def anubis(request):
    granadas = Granada.objects.filter(nome_mapa='Anubis')
    return render(request, 'anubis.html', {'granadas': granadas})

@login_required
def nuke(request):
    granadas = Granada.objects.filter(nome_mapa='Nuke')
    return render(request, 'nuke.html', {'granadas': granadas})

@login_required
def ancient(request):
    granadas = Granada.objects.filter(nome_mapa='Ancient')
    return render(request, 'ancient.html', {'granadas': granadas})
