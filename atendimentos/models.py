from django.db import models

from servicos.models import Servico
from clientes.models import Cliente

class Atendimento(models.Model):

    servico = models.ForeignKey(Servico, on_delete = models.CASCADE)
    atendente = models.CharField(max_length=100)
    helper = models.CharField(max_length=100)
    valor_pago = models.DecimalField(max_digits = 7, decimal_places = 2)

    FORMA_PAGAMENTO = (

        ('D', 'Dinheiro'),
        ('P', 'PIX'),
        ('CD', 'Cartao Débito'),
        ('CC', 'Cartao Crédito')
    )

    forma_pgto = models.CharField(max_length= 2, choices=FORMA_PAGAMENTO, blank= False, null= False, default= 1)
    data_atendimento = models.DateTimeField(auto_now_add = True)
    data_agendada = models.DateTimeField(auto_now_add = False, blank= False, null= False)

    SITUACAO = (

        (1, 'PENDENTE'),
        (2, 'REALIZADO'),
        (3, 'CANCELADO')

    )

    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.cliente.nome