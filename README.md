
## Executando o Aplicativo

Com Poetry:

```bash
# Instalar dependências
poetry install

# Executar o aplicativo
poetry run task run
# ou
poetry run python -m fastapi_zero.main
```

Para desenvolvimento, você pode usar o modo de recarga automática:

```bash
poetry run uvicorn fastapi_zero.main:app --reload
```

## Estrutura do Projeto

```
fastapi_zero/
├── __init__.py
├── main.py                  # Ponto de entrada principal
├── core/                    # Configurações e utilitários centrais
│   ├── __init__.py
│   └── config.py            # Configurações da aplicação
├── routers/                 # Routers para diferentes partes da aplicação
│   ├── __init__.py
│   ├── api.py               # Endpoints da API
│   └── pages.py             # Páginas HTML
├── models/                  # Modelos de dados
│   └── __init__.py
├── schemas/                 # Esquemas Pydantic
│   ├── __init__.py
│   └── schemas.py           # Esquemas de dados
├── services/                # Lógica de negócios
│   └── __init__.py
└── templates/               # Templates HTML
```


