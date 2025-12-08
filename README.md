# Plataforma de Imputação Pluviométrica (Async)

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)

## Visão Geral
Plataforma web para processamento **assíncrono** de séries temporais pluviométricas, focada na detecção de falhas, validação de consistência e **imputação de dados meteorológicos**.  
O sistema foi projetado para suportar grandes volumes de dados históricos mantendo a interface responsiva por meio de workers assíncronos.

---

## Objetivo
Fornecer uma solução robusta e extensível para:
- Ingestão de dados meteorológicos (CSV/XLS)
- Detecção automática de falhas (gaps)
- Validação de consistência física
- Imputação por múltiplos métodos
- Comparação e auditoria de experimentos
- Exportação de dados tratados e métricas

---

## Arquitetura
- **Backend:** Django + Django REST Framework
- **Processamento Assíncrono:** Celery
- **Broker / Backend:** Redis
- **Banco de Dados:** PostgreSQL
- **Padrão Arquitetural:** Producer–Consumer
- **Comunicação:** REST API + polling de status

---

## Funcionalidades
- Upload de arquivos meteorológicos
- Processamento assíncrono (não bloqueante)
- Acompanhamento do status da tarefa
- Regras de consistência (ex.: chuva ≥ 0)
- Múltiplos métodos de imputação:
  - Média
  - Regressão
  - IDW
- Registro de experimentos
- Cálculo de métricas (RMSE, MAE, R²)
- Exportação de resultados

---

## Modelo de Dados (Resumo)
- Estação
- Medição Bruta
- Medição Tratada
- Experimento de Imputação
- Relatório Experimental
- Tarefa de Processamento

---

## Execução Local (Docker)
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
docker compose up --build
```

---

## API (Resumo)
- `POST /api/v1/upload/` – Envio de arquivo
- `GET /api/v1/tasks/{id}` – Status da tarefa
- `GET /api/v1/results/{id}` – Exportação dos dados

---

## Testes
- Testes unitários dos métodos de imputação
- Testes de consistência e determinismo
- Testes de integração da API

---

## Roadmap
- [x] Arquitetura base
- [x] Pipeline assíncrono
- [ ] Interface Web
- [ ] Métodos baseados em redes neurais
- [ ] Deploy em nuvem

---

## Autor
**Eugênio José Moura Neto**  
Projeto acadêmico / Iniciação Científica

---

## Licença
Este projeto está licenciado sob a licença MIT.
