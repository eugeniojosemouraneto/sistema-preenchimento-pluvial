# Usa Python 3.11 na versão slim (mais leve)
FROM python:3.11-slim

# Impede que o Python guarde ficheiros .pyc e garante logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema necessárias para compilar pacotes Python (ex: psycopg2)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o ficheiro de dependências e instala
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte da pasta backend para dentro do container
COPY . /app/

# O comando final será definido no docker-compose (web ou worker)