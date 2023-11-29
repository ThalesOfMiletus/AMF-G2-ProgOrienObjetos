from django.contrib import admin
from .models import *
# Register your models here.

class GranadaAdmin(admin.ModelAdmin):
    list_display = ('nome_mapa', 'tipo_granada', 'bomb', 'link')

admin.site.register(Granada, GranadaAdmin)