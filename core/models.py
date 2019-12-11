from django.db import models
from django.contrib.auth.models import User


class Forum (models.Model):
    pergunta = models.CharField('Pergunta', max_length=5000)
    resposta = models.CharField('Resposta', max_length=10000, null=True, blank=True)
# Create your models here.


class Servico(models.Model):
    descricao = models.CharField("Descrição", max_length=500)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2)


class ClienteServico(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    horario = models.DateTimeField("Horário")
