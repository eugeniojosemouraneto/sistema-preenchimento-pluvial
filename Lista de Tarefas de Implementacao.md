# Fase 0: Configuração do Ambiente e Infraestrutura

## 0.1 — Estrutura de Diretórios e Git

**Objetivo curto:** Estabelecer a base do projeto e controle de versão.

**Passos executáveis:**
- Crie a pasta raiz `plataforma-meteo` e entre nela.
- Inicialize o git: `git init`.
- Crie o arquivo `.gitignore` na raiz com as exceções (`venv/`, `__pycache__/`, `.env`, `media/`, `db.sqlite3`).
- Crie a estrutura de pastas inicial:
```bash
mkdir -p data/db media/uploads
```

**Validação:**
- `git status` mostra o repositório limpo/inicializado.
- `ls -R` mostra as pastas `data` e `media`.

---

## 0.2 — Ambiente Virtual e Dependências

**Objetivo curto:** Isolar as bibliotecas Python do projeto.

**Passos executáveis:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install django celery redis psycopg2-binary pandas numpy pandera scikit-learn django-environ
pip freeze > requirements.txt
```

---

## 0.3 — Inicialização do Django

**Objetivo curto:** Criar a estrutura do framework e o app principal.

**Passos executáveis:**
```bash
django-admin startproject core .
python manage.py startapp pluviometria
```

---

## 0.4 — Docker Compose (Infraestrutura)

**Objetivo curto:** Orquestrar Banco de Dados, Redis, Web e Workers.

**Passos executáveis:**
- Criar `Dockerfile` baseado em Python 3.11 slim.
- Criar `docker-compose.yml` com serviços: db (Postgres), redis, web (Django) e worker (Celery).
- Validar:
```bash
docker-compose config
```

---

# Fase 1: Modelagem de Dados e Admin

## 1.1 — Configurar Conexão com Banco

**Objetivo curto:** Conectar o Django ao PostgreSQL do Docker.

**Passos executáveis:**
- Configurar variáveis de ambiente no `settings.py`.
- Alterar `DATABASES` para PostgreSQL (host `db`).

---

## 1.2 — Implementar Models

**Objetivo curto:** Traduzir o diagrama ER em models Django.

**Passos executáveis:**
- Criar models: `Estacao`, `MedicaoBruta`, `TarefaProcessamento`, `RelatorioExperimento`, `MedicaoTratada`.

---

## 1.3 — Migrações

**Objetivo curto:** Criar tabelas no banco.

**Passos executáveis:**
```bash
python manage.py makemigrations pluviometria
python manage.py migrate
```

---

## 1.4 — Configurar Django Admin

**Objetivo curto:** Administração de dados.

**Passos executáveis:**
```bash
python manage.py createsuperuser
```

---

# Fase 2: Backend Síncrono (Upload)

## 2.1 — Configurar Media

**Objetivo curto:** Permitir upload de arquivos.

**Passos executáveis:**
- Definir `MEDIA_URL` e `MEDIA_ROOT`.
- Configurar `urls.py`.

---

## 2.2 — Formulário de Upload

**Objetivo curto:** Validar arquivos.

**Passos executáveis:**
- Criar `UploadArquivoForm` com validação de extensão.

---

## 2.3 — View de Upload

**Objetivo curto:** Criar tarefa e salvar arquivo.

**Passos executáveis:**
- Criar `upload_view`.
- Retornar JSON com `task_id`.

---

## 2.4 — Roteamento

**Objetivo curto:** Expor endpoint.

**Passos executáveis:**
- Criar rotas em `pluviometria/urls.py`.

---

# Fase 3: Configuração do Celery

## 3.1 — Celery App

**Objetivo curto:** Inicializar Celery.

**Passos executáveis:**
- Criar `core/celery.py`.

---

## 3.2 — Integração com Django

**Objetivo curto:** Carregar Celery no boot.

**Passos executáveis:**
- Importar celery em `core/__init__.py`.

---

## 3.3 — Settings do Celery

**Objetivo curto:** Conectar ao Redis.

**Passos executáveis:**
- Definir `CELERY_BROKER_URL`.

---

## 3.4 — Smoke Test

**Objetivo curto:** Verificar comunicação.

**Passos executáveis:**
```bash
docker-compose up --build
```

---

# Fase 4: Tasks

## 4.1 — Estrutura da Task

**Objetivo curto:** Processamento assíncrono.

**Passos executáveis:**
- Criar task com `@shared_task`.

---

## 4.2 — Leitura e Sanitização

**Objetivo curto:** Carregar CSV.

**Passos executáveis:**
- Ler com Pandas.
- Validar colunas.

---

## 4.3 — Lógica e Persistência

**Objetivo curto:** Imputar e salvar dados.

**Passos executáveis:**
- Criar objetos em lote.
- Usar `bulk_create`.

---

# Fase 5: Frontend

## 5.1 — View de Status

**Objetivo curto:** Consultar progresso.

**Passos executáveis:**
- Criar `status_view`.

---

## 5.2 — HTML e JS

**Objetivo curto:** Polling simples.

**Passos executáveis:**
- Criar `upload.html`.
- JS com `setInterval`.

---

# Fase 6: Testes

## 6.1 — Teste Manual

**Objetivo curto:** Validar fluxo.

**Passos executáveis:**
- Testar CSV válido e inválido.

---

## 6.2 — Teste de Carga

**Objetivo curto:** Concorrência leve.

**Passos executáveis:**
- Enviar múltiplos arquivos.


