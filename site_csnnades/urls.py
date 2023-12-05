from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastrar_granada/<str:mapa_slug>/', views.cadastrar_granada, name='cadastrar_granada'),
    path('mirage', views.mirage, name='mirage'),
    path('nuke', views.nuke, name='nuke'),
    path('inferno', views.inferno, name='inferno'),
    path('ancient', views.ancient, name='ancient'),
    path('anubis', views.anubis, name='anubis'),
    path('overpass', views.overpass, name='overpass'),
    path('vertigo', views.vertigo, name='vertigo'),
    path('home', views.home, name='home'),
]
