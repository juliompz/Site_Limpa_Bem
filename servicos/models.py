from django.db import models


class Servico(models.Model):

    nome = models.CharField(max_length = 255)
    valor = models.DecimalField(max_digits = 7, decimal_places = 2)
    descricao = models.TextField(default='Descrição')

    def __str__(self):
        return self.nome
 

