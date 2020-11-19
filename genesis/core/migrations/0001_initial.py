# Generated by Django 3.0.2 on 2020-10-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='GENESIS', max_length=30)),
                ('descripcion', models.TextField(default='')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='genesis')),
                ('titulo', models.CharField(max_length=50)),
                ('directorio', models.CharField(max_length=200)),
                ('directoriogenesis', models.CharField(default='', max_length=200)),
                ('directoriotexto', models.CharField(default='', max_length=200)),
                ('directoriozip', models.CharField(default='', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=50)),
                ('descripcion', models.TextField(default='')),
                ('importe', models.CharField(default='', max_length=10)),
                ('paypal', models.TextField(default='')),
            ],
        ),
    ]
