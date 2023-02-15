from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group

from servicos.models import Servico
from clientes.models import Cliente



class Atendimento(models.Model):

    servico = models.ForeignKey(Servico, on_delete = models.DO_NOTHING)

    atendente = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
        limit_choices_to={'groups__name': 'Atendente'}, related_name='Atendente')

    helper = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        limit_choices_to={'groups__name': 'Helper'},  related_name='Helper')

    FORMA_PAGAMENTO = (

        ('D', 'Dinheiro'),
        ('P', 'PIX'),
        ('CD', 'Cartao Débito'),
        ('CC', 'Cartao Crédito')
    )

    GERENTE_DESCONTO = (
        ('S', 'SIM'),
        ('N', 'NÃO')
    )

    gerente_desc = models.CharField(max_length= 1, 
                                    choices=GERENTE_DESCONTO, blank=False,
                                    null=False, default='N')    

    forma_pgto = models.CharField(max_length= 2, choices=FORMA_PAGAMENTO, 
                                    blank= False, null= False, 
                                    default= 'D')

    data_atendimento = models.DateTimeField(auto_now_add = True)
    data_agendada = models.DateTimeField(auto_now_add = False, blank= False, null= False)

    SITUACAO = (

        ('P', 'PENDENTE'),
        ('R', 'REALIZADO'),
        ('C', 'CANCELADO')

    )
    
    situacao = models.CharField(max_length=1, choices=SITUACAO, 
                                blank=False, null=False, 
                                default='P')
    cliente = models.ForeignKey(Cliente, on_delete= models.DO_NOTHING)

    def __str__(self) -> str:
        return self.cliente.nome