from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do Funcionario")


    def __str__(self) -> str:
        return self.nome