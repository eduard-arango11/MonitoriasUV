# Generated by Django 2.0.7 on 2018-08-27 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Facultades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramaAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_programa', models.CharField(max_length=200, unique=True, verbose_name='Nombre del programa')),
                ('codigo_programa', models.PositiveIntegerField(unique=True, verbose_name='Codigo del programa')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado')),
                ('jornada', models.CharField(choices=[('Diurna', 'Diurna'), ('Nocturna', 'Nocturna'), ('Vespertina', 'Vespertina')], default='Diurna', max_length=20, verbose_name='Jornada')),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facultades.Facultad')),
            ],
        ),
    ]
