# Generated by Django 4.1.6 on 2023-02-15 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0010_atendimento_valor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='forma_pgto',
            new_name='formapgto',
        ),
    ]
