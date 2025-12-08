from django.db import models


class Estacao(models.Model):
    nome = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # Armazena regras como {"min": 0, "max": 400, "max_delta": 100}
    limites_fisicos = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.nome
