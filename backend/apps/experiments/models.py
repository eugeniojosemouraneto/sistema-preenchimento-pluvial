from django.db import models
from apps.processing.models import TarefaProcessamento
from apps.ingestion.models import MedicaoBruta


class RelatorioExperimento(models.Model):
    task = models.ForeignKey(TarefaProcessamento, on_delete=models.CASCADE)
    metodo_utilizado = models.CharField(max_length=50)  # Ex: IDW, REGRESSAO
    parametros_execucao = models.JSONField()  # Ex: {"k_vizinhos": 3}
    versao_algoritmo = models.CharField(max_length=20, default="v1.0")
    data_execucao = models.DateTimeField(auto_now_add=True)


class MedicaoTratada(models.Model):
    class TipoDado(models.TextChoices):
        REAL = "REAL", "Real"
        ESTIMADO = "ESTIMADO", "Estimado"

    medicao_bruta = models.ForeignKey(MedicaoBruta, on_delete=models.CASCADE)
    experimento = models.ForeignKey(RelatorioExperimento, on_delete=models.CASCADE)
    valor_preenchido = models.FloatField()
    tipo_dado = models.CharField(max_length=20, choices=TipoDado.choices)


class ValidacaoMetrica(models.Model):
    experimento = models.ForeignKey(
        RelatorioExperimento, on_delete=models.CASCADE, related_name="metricas"
    )
    metrica = models.CharField(max_length=50)  # Ex: R2, RMSE
    valor = models.FloatField()
