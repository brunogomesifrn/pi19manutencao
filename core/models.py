from django.db import models

class Forum (models.Model):
	pergunta = models.CharField('Pergunta', max_length=5000)
	resposta = models.CharField('Resposta', max_length=10000, null=True, blank=True)
# Create your models here.
