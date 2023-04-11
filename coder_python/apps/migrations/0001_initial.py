# Generated by Django 4.1.5 on 2023-04-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcliente', models.IntegerField()),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=40)),
                ('usuario', models.CharField(max_length=40)),
                ('clave', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproducto', models.IntegerField()),
                ('idcliente', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproducto', models.IntegerField()),
                ('item', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('local', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
