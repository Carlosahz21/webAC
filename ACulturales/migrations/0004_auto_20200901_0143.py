# Generated by Django 3.1 on 2020-09-01 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ACulturales', '0003_auto_20200831_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agrupacion',
            old_name='id_ambito',
            new_name='ambito',
        ),
        migrations.RenameField(
            model_name='agrupacion',
            old_name='id_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='agrupacion',
            old_name='id_parroquia',
            new_name='parroquia',
        ),
    ]
