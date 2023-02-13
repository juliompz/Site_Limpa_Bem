# Generated by Django 4.1.6 on 2023-02-13 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicos', '0002_remove_servico_tipo_servico_descricao_servico_nome_and_more'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atendente', models.CharField(max_length=100)),
                ('helper', models.CharField(max_length=100)),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=7)),
                ('forma_pgto', models.CharField(choices=[('D', 'Dinheiro'), ('P', 'PIX'), ('CD', 'Cartao Débito'), ('CC', 'Cartao Crédito')], default=1, max_length=2)),
                ('data_atendimento', models.DateTimeField(auto_now_add=True)),
                ('data_agendada', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servico')),
            ],
        ),
    ]