from django.db import models
from apps.funcionarios.models import Funcionario



class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text="Motivo da hora extra")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.motivo