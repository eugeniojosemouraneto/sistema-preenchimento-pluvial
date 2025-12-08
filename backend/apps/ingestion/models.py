from django.db import models
from apps.stations.models import Estacao


class MedicaoBruta(models.Model):
    class StatusConsistencia(models.TextChoices):
        OK = "OK", "Ok"
        SUSPEITO = "SUSPEITO", "Suspeito"
        ERRO = "ERRO", "Erro"

    estacao = models.ForeignKey(
        Estacao, on_delete=models.CASCADE, related_name="medicoes"
    )
    data = models.DateField(db_index=True)
    valor = models.FloatField(null=True, blank=True)
    flag_consistencia = models.CharField(
        max_length=20, choices=StatusConsistencia.choices, default=StatusConsistencia.OK
    )
    # Hash MD5 para evitar reprocessamento do mesmo ficheiro
    hash_arquivo = models.CharField(max_length=32, db_index=True)

    def __str__(self):
        return f"{self.estacao} - {self.data}"
