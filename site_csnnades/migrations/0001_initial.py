# Generated by Django 4.2.7 on 2023-11-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('mapa', models.CharField(choices=[('Mirage', 'Mirage'), ('Inferno', 'Inferno'), ('Overpass', 'Overpass'), ('Nuke', 'Nuke'), ('Vertigo', 'Vertigo'), ('Anubis', 'Anubis'), ('Ancient', 'Ancient')], max_length=100)),
            ],
        ),
    ]
