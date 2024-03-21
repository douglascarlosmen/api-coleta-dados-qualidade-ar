# API de Recepção de Dados de Qualidade do Ar

Esta aplicação Flask serve como uma API simples para receber e armazenar dados de qualidade do ar enviados por sensores IoT. Os dados são mantidos em memória para simplificação, facilitando o teste e a demonstração do fluxo de dados.

## Funcionalidades

- **Recepção de Dados**: Endpoint para receber dados via POST em formato JSON.
- **Armazenamento Temporário**: Dados recebidos são armazenados em uma lista em memória.
- **Recuperação de Dados**: Endpoint para recuperar os dados armazenados via GET.
- **Processamento Básico de Dados**: Função esqueleto para implementar lógica de processamento dos dados recebidos.

## Como Usar

### Requisitos

- Python 3.x
- Flask

### Instalação

Instale o Flask utilizando o pip, se ainda não estiver instalado:

```bash
pip install Flask
```

### Executando a Aplicação
Para iniciar a API, execute o script Python na linha de comando:

```python
python coleta-dados.py
```

Isso iniciará o servidor de desenvolvimento Flask na porta 5000.

### Enviando Dados para a API

Para enviar dados para a API, faça uma requisição POST para http://localhost:5000/dados com um payload JSON. Por exemplo:

```json
{
  "sensor_id": 1,
  "data": {
    "CO2": 415,
    "PM2_5": 10,
    "temperature": 25,
    "humidity": 40
  }
}
```

Você pode usar ferramentas como Postman, curl ou qualquer cliente HTTP de sua escolha para fazer a requisição.

### Recuperando Dados Armazenados

Para visualizar os dados que foram armazenados pela API, faça uma requisição GET para http://localhost:5000/dados. Isso retornará todos os dados que foram enviados à API até o momento.

### Desenvolvimento Futuro

Este projeto é uma base para experimentos e prototipagem rápida. Para uso em ambientes de produção ou desenvolvimento adicional, considere:

- Substituir o armazenamento em memória por um banco de dados persistente.
- Implementar autenticação e autorização para proteger os endpoints.
- Adicionar validação de dados para garantir a integridade e a formatação correta dos dados recebidos.
- Expandir a lógica de processamento de dados para incluir análises mais complexas.