# Generated by Django 4.1.6 on 2023-02-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0006_alter_atendimento_atendente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='valor',
            field=models.IntegerField(default=models.F('servico__valor')),
        ),
    ]
