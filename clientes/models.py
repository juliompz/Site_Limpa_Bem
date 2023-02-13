from django.db import models

class Cliente(models.Model):

    nome = models.CharField(max_length= 255)
    telefone = models.CharField(max_length= 25)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
