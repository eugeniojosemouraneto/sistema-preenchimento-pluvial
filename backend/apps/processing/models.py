from django.db import models
import uuid


class TarefaProcessamento(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pendente"
        STARTED = "STARTED", "Iniciado"
        SUCCESS = "SUCCESS", "Sucesso"
        FAILURE = "FAILURE", "Falha"

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING, db_index=True
    )
    progresso = models.IntegerField(default=0)  # 0 a 100
    log_erros = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.task_id} ({self.status})"
