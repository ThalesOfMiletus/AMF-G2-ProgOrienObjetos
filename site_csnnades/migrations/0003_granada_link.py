# Generated by Django 4.2.7 on 2023-11-27 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_csnnades', '0002_granada_delete_videopost'),
    ]

    operations = [
        migrations.AddField(
            model_name='granada',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
