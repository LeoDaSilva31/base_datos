# Generated by Django 5.0.6 on 2024-06-05 19:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('archivo_pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('creado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creado_por', to=settings.AUTH_USER_MODEL)),
                ('editado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editado_por', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
