# Generated by Django 3.1.1 on 2021-06-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinos', '0005_auto_20210611_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinosaur',
            name='period',
            field=models.CharField(choices=[('unknown', 'UnKnown'), ('Late Triassic', 'Late Triassic'), ('Early Jurassic', 'Early Jurassic'), ('Mid Jurassic', 'Mid Jurassic'), ('Late Jurassic', 'Late Jurassic'), ('Early Cretaceous', 'Early Cretaceous'), ('Late Cretaceous', 'Late Cretaceous')], default='unknown', max_length=25, verbose_name='Period of time when dinosaur lived'),
        ),
        migrations.AlterField(
            model_name='dinosaur',
            name='typeofdino',
            field=models.CharField(choices=[('unknown', 'UnKnown'), ('Armoured dinosaurs', 'Armoured Dinosaurs'), ('Ceratopsian', 'Ceratopsian'), ('Euornithopod', 'Euornithopod'), ('Sauropod', 'Sauropod'), ('Large theropod', 'Large Theropod'), ('Small theropod', 'Small Theropod')], default='unknown', max_length=25, verbose_name='Type of Dinosaur'),
        ),
    ]
