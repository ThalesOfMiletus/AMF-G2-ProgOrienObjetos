from django.db import models
from embed_video.fields import EmbedVideoField

class Granada(models.Model):
    MAP_CHOICES = [
    ('Mirage', 'Mirage'),
    ('Inferno', 'Inferno'),
    ('Overpass', 'Overpass'),
    ('Nuke', 'Nuke'),
    ('Vertigo', 'Vertigo'),
    ('Anubis', 'Anubis'),
    ('Ancient', 'Ancient'),
    ]

    TIPO_CHOICES = [
        ('Smoke', 'Smoke'),
        ('Flash', 'Flash'),
        ('HE', 'High Explosive (HE)'),
        ('Molotov', 'Molotov'),
    ]

    BOMB_CHOICES = [
        ('Bomb A', 'Bomb A'),
        ('Bomb B', 'Bomb B'),
        ('Meio', 'Meio'),
    ]

    nome_mapa = models.CharField(max_length=50, choices=MAP_CHOICES)
    tipo_granada = models.CharField(max_length=20, choices=TIPO_CHOICES)
    bomb = models.CharField(max_length=30, choices=BOMB_CHOICES)
    link = EmbedVideoField(blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_granada} em {self.nome_mapa} para {self.get_bomb_display()}"