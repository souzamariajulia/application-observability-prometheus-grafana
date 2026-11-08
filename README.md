
# Observabilidade de Aplicações com Prometheus e Grafana

Projeto prático de observabilidade de aplicações utilizando Python, Flask, Prometheus, Grafana e Docker Compose.

## Sobre o Projeto

Este projeto demonstra como monitorar uma aplicação web desenvolvida em Python, realizando a coleta de métricas, análise de desempenho, identificação de erros HTTP e visualização de indicadores por meio de dashboards no Grafana.

## Arquitetura

```text
Aplicação Python (Flask)
          |
          | Exposição de métricas
          v
      Prometheus
          |
          | Consulta de métricas com PromQL
          v
       Grafana
          |
          v
    Dashboard de Observabilidade

Docker Compose gerencia os serviços.
```

## Tecnologias Utilizadas

- Python
- Flask
- Prometheus
- PromQL
- Grafana
- Docker
- Docker Compose

## Métricas Monitoradas

- Total de requisições HTTP.
- Taxa de requisições por segundo.
- Total de erros HTTP 5xx.
- Tempo de resposta da aplicação.
- Latência P95 das requisições.

## Endpoints da Aplicação

| Endpoint | Descrição |
|---|---|
| `/` | Verifica o funcionamento da aplicação |
| `/health` | Verificação de saúde da aplicação |
| `/slow` | Simula uma resposta lenta |
| `/simulate-error` | Simula um erro HTTP 500 |
| `/metrics` | Disponibiliza métricas para o Prometheus |

## Como Executar o Projeto

Pré-requisitos:
- Docker instalado.
- Docker Compose disponível.

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/application-observability-prometheus-grafana.git
```

Acesse a pasta do projeto:

```bash
cd application-observability-prometheus-grafana
```

Inicie os serviços:

```bash
docker compose up -d
```

## Acesso aos Serviços

| Serviço | Endereço |
|---|---|
| Aplicação Python | http://localhost:5000 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

Credenciais locais do Grafana:

- Usuário: `admin`
- Senha: `admin`

## Dashboard de Observabilidade

As capturas de tela do dashboard Grafana e do ambiente de monitoramento estarão disponíveis na pasta `screenshots/`.

## Objetivos de Aprendizado

- Compreender os conceitos de observabilidade de aplicações.
- Instrumentar aplicações com métricas do Prometheus.
- Realizar coleta e consulta de métricas utilizando Prometheus e PromQL.
- Construir dashboards de monitoramento com Grafana.
- Containerizar serviços utilizando Docker.
- Configurar regras de alerta para identificação de erros na aplicação.
