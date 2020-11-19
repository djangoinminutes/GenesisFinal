# Generated by Django 3.0.2 on 2020-10-15 19:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aplicaciones', '0001_initial'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', ckeditor.fields.RichTextField(default='')),
                ('padre', models.CharField(default='nada', max_length=30)),
                ('nombreself', models.CharField(default='', max_length=100)),
                ('nombreborrar', models.CharField(default='', max_length=100)),
                ('textoopcionmenu', models.CharField(blank=True, default='', max_length=30)),
                ('modeloenmenu', models.BooleanField(default=True)),
                ('sinbasedatos', models.BooleanField(default=False)),
                ('imagenmenu', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('tooltip', models.CharField(blank=True, default='', max_length=30)),
                ('ordengeneracion', models.SmallIntegerField(default=1)),
                ('ultimoregistro', models.CharField(blank=True, default='p', max_length=1)),
                ('titulolista', models.CharField(blank=True, default='Lista de registros', max_length=30)),
                ('fonttitulolista', models.CharField(default='Roboto,18,700', max_length=100)),
                ('colorfondotitulolista', models.CharField(default='transparent', max_length=20)),
                ('colortitulolista', models.CharField(default='#1a1a1a', max_length=20)),
                ('altotitulolista', models.SmallIntegerField(default=40)),
                ('mayusculastitulolista', models.BooleanField(default=False)),
                ('justificacionverticaltitulolista', models.CharField(default='c', max_length=1)),
                ('justificacionhorizontaltitulolista', models.CharField(default='i', max_length=1)),
                ('fontcomentariolista', models.CharField(default='Open+Sans,10,normal', max_length=100)),
                ('comentariolista', models.CharField(blank=True, default='', max_length=200)),
                ('colorfondocomentariolista', models.CharField(default='transparent', max_length=20)),
                ('colorcomentariolista', models.CharField(default='#3a3a3a', max_length=20)),
                ('mayusculascolumnas', models.BooleanField(default=False)),
                ('altocolumnas', models.SmallIntegerField(default=30)),
                ('colorfondocolumnaslista', models.CharField(default='#eeeeee', max_length=20)),
                ('colorcolumnaslista', models.CharField(default='#2a2a2a', max_length=20)),
                ('fontcolumnaslista', models.CharField(default='Roboto,10,700', max_length=100)),
                ('columnaslistaconborde', models.BooleanField(default=False)),
                ('fonttextolista', models.CharField(default='Arial,10,normal', max_length=100)),
                ('colorfondotextolista', models.CharField(default='transparent', max_length=20)),
                ('colortextolista', models.CharField(default='#2a2a2a', max_length=20)),
                ('buscadorlista', models.BooleanField(default=False)),
                ('fonteditarborrar', models.CharField(default='Arial,10,normal', max_length=100)),
                ('coloreditarborrar', models.CharField(default='blue', max_length=20)),
                ('textoeditarborrar', models.CharField(default='Editar,Borrar', max_length=30)),
                ('fontlinknuevomodelo', models.CharField(default='Arial,12,700', max_length=100)),
                ('colorlinknuevomodelo', models.CharField(default='#ffeeaa', max_length=20)),
                ('colorbotonlinknuevomodelo', models.CharField(default='primary', max_length=20)),
                ('textolinknuevomodelo', models.CharField(default='Nuevo registro', max_length=30)),
                ('linknuevomodelo', models.BooleanField(default=True)),
                ('reportsize', models.CharField(default='L', max_length=20)),
                ('reportorientation', models.CharField(default='P', max_length=20)),
                ('titulox', models.DecimalField(decimal_places=2, default=10.5, max_digits=5)),
                ('fechax', models.DecimalField(decimal_places=2, default=10.5, max_digits=5)),
                ('lineaix', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('lineafx', models.DecimalField(decimal_places=2, default=20.5, max_digits=5)),
                ('grosorlinea', models.DecimalField(decimal_places=2, default=0.3, max_digits=5)),
                ('datoinicialx', models.DecimalField(decimal_places=2, default=1.5, max_digits=5)),
                ('identacionautomatica', models.BooleanField(default=True)),
                ('tituloinserta', models.CharField(default='Nuevo Modelo', max_length=30)),
                ('fonttituloinserta', models.CharField(default='Roboto,18,700', max_length=100)),
                ('colortituloinserta', models.CharField(default='#1a1a1a', max_length=20)),
                ('colorfondotituloinserta', models.CharField(default='transparent', max_length=20)),
                ('colorfondofilatituloinserta', models.CharField(default='transparent', max_length=20)),
                ('altofilatituloinserta', models.SmallIntegerField(default=40)),
                ('justificacionverticaltituloinserta', models.CharField(default='c', max_length=1)),
                ('justificacionhorizontaltituloinserta', models.CharField(default='i', max_length=1)),
                ('colorfondocomentarioinserta', models.CharField(default='transparent', max_length=20)),
                ('colorcomentarioinserta', models.CharField(default='#3a3a3a', max_length=20)),
                ('fontcomentarioinserta', models.CharField(default='Open+Sans,10,normal', max_length=100)),
                ('comentarioinserta', models.CharField(blank=True, default='', max_length=200)),
                ('numerocolumnasizquierdainserta', models.SmallIntegerField(default=1)),
                ('numerocolumnasmodeloinserta', models.SmallIntegerField(default=10)),
                ('numerocolumnasderechainserta', models.SmallIntegerField(default=1)),
                ('tituloupdate', models.CharField(default='Modelo a editar: ', max_length=30)),
                ('fonttituloupdate', models.CharField(default='Roboto,18,700', max_length=100)),
                ('colortituloupdate', models.CharField(default='#1a1a1a', max_length=20)),
                ('colorfondotituloupdate', models.CharField(default='transparent', max_length=20)),
                ('colorfondofilatituloupdate', models.CharField(default='transparent', max_length=20)),
                ('altofilatituloupdate', models.SmallIntegerField(default=40)),
                ('justificacionverticaltituloupdate', models.CharField(default='c', max_length=1)),
                ('justificacionhorizontaltituloupdate', models.CharField(default='i', max_length=1)),
                ('comentarioupdate', models.CharField(blank=True, default='', max_length=200)),
                ('colorfondocomentarioupdate', models.CharField(default='transparent', max_length=20)),
                ('fontcomentarioupdate', models.CharField(default='Open+Sans,10,normal', max_length=100)),
                ('colorcomentarioupdate', models.CharField(default='#3a3a3a', max_length=20)),
                ('numerocolumnasizquierdaupdate', models.SmallIntegerField(default=1)),
                ('numerocolumnasderechaupdate', models.SmallIntegerField(default=1)),
                ('numerocolumnasmodeloupdate', models.SmallIntegerField(default=10)),
                ('fontlabelmodelo', models.CharField(default='Arial,10,bold', max_length=100)),
                ('colorlabelmodelo', models.CharField(default='#010203', max_length=20)),
                ('controlesautomaticos', models.BooleanField(default=False)),
                ('tituloborra', models.CharField(blank=True, default='Borrar el modelo', max_length=30)),
                ('fonttituloborra', models.CharField(default='Roboto,18,700', max_length=100)),
                ('colortituloborra', models.CharField(default='#1a1a1a', max_length=20)),
                ('colorfondotituloborra', models.CharField(default='transparent', max_length=20)),
                ('colorfondofilatituloborra', models.CharField(default='transparent', max_length=20)),
                ('altofilatituloborra', models.SmallIntegerField(default=40)),
                ('justificacionverticaltituloborra', models.CharField(default='c', max_length=1)),
                ('justificacionhorizontaltituloborra', models.CharField(default='i', max_length=1)),
                ('colorfondocomentarioborra', models.CharField(default='transparent', max_length=20)),
                ('colorcomentarioborra', models.CharField(default='#3a3a3a', max_length=20)),
                ('fontcomentarioborra', models.CharField(default='Open+Sans,10,normal', max_length=100)),
                ('comentarioborra', models.CharField(blank=True, default='', max_length=200)),
                ('colorfondotextoborra', models.CharField(default='#eaebec', max_length=20)),
                ('colortextoborra', models.CharField(default='#1a1a1a', max_length=20)),
                ('fonttextoborra', models.CharField(default='Arial,10,normal', max_length=100)),
                ('textoborra', models.CharField(blank=True, default='Borrar el modelo:', max_length=200)),
                ('textobotonborra', models.CharField(blank=True, default='Borrar', max_length=30)),
                ('numerocolumnasizquierdaborra', models.SmallIntegerField(default=1)),
                ('numerocolumnasderechaborra', models.SmallIntegerField(default=1)),
                ('numerocolumnasmodeloborra', models.SmallIntegerField(default=10)),
                ('hijoscontiguos', models.BooleanField(default=False)),
                ('numerocolumnashijosupdate', models.SmallIntegerField(default=5)),
                ('listastaff', models.BooleanField(default=False)),
                ('listalogin', models.BooleanField(default=False)),
                ('crearstaff', models.BooleanField(default=False)),
                ('crearlogin', models.BooleanField(default=False)),
                ('editarstaff', models.BooleanField(default=False)),
                ('editarlogin', models.BooleanField(default=False)),
                ('borrarstaff', models.BooleanField(default=False)),
                ('borrarlogin', models.BooleanField(default=False)),
                ('numerocolumnaslabels', models.SmallIntegerField(default=5)),
                ('numerocolumnascontroles', models.SmallIntegerField(default=7)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('aplicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.Aplicacion')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyecto')),
            ],
        ),
    ]
