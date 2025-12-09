import os
from celery import Celery

# Define o módulo de settings padrão do Django para o 'celery'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# Lê as configurações do Django começando com 'CELERY_' no settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Descobre tarefas (tasks.py) em todos os apps instalados automaticamente
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
