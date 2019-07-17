# Generated by Django 2.2.3 on 2019-07-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crear_personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='personas',
            fields=[
                ('id_persona', models.BigIntegerField(db_column='id_persona', primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='nombre')),
                ('apellido', models.TextField(db_column='apellido')),
                ('direccion', models.TextField(db_column='direccion')),
                ('activo', models.BooleanField(db_column='activo')),
                ('telefono', models.CharField(db_column='telefono', max_length=10)),
                ('fecha_nac', models.DateField(db_column='fecha_nac', max_length=10)),
            ],
            options={
                'db_table': 'personas',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='persona',
        ),
    ]
