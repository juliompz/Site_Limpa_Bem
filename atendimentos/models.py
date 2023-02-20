from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.db.models import F

from servicos.models import Servico
from clientes.models import Cliente



class Atendimento(models.Model):

    servico = models.ForeignKey(Servico, on_delete = models.CASCADE)

    atendente = models.ForeignKey(
                                settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
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


    formapgto = models.CharField(max_length= 2, choices=FORMA_PAGAMENTO, 
                                    blank= False, null= False, 
                                    default= 'D')

    def get_formapgto_display(self):
        return dict(self.FORMA_PAGAMENTO)[self.formapgto]

    GERENTE_DESCONTO = (
        ('S', 'Sim'),
        ('N', 'Não')
    )

    gerente_desc = models.CharField(max_length= 1, 
                                    choices=GERENTE_DESCONTO, blank=False,
                                    null=False, default='N')    
    
    def get_gerente_desc_display(self):
        return dict(self.GERENTE_DESCONTO)[self.gerente_desc]

    valor = models.DecimalField(max_digits=10, decimal_places=2, 
                                editable=False, default= 0.0)

    def save(self):
        self.valor = self.servico.valor
        super().save()


    data_atendimento = models.DateTimeField(auto_now_add= True)
    data_agendada = models.DateTimeField(auto_now_add = False, 
                                        blank= False, null= False)

    SITUACAO = (

        ('P', 'Pendente'),
        ('R', 'Realizado'),
        ('C', 'Cancelado')

    )
    
    situacao = models.CharField(max_length=1, choices=SITUACAO, 
                                blank=False, null=False, 
                                default='P')

    def get_situacao_display(self):
        return dict(self.SITUACAO)[self.situacao]    
        
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)

    def __str__(self):
        return str('Atendimento CLIENTE: ' + self.cliente.nome)

