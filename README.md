# GLOBO - Teste

Resolução do teste técnico para a vaga de Desenvolvedor Backend - Produtos de dados


## Pré-requisitos

- Python 3.12.x
- Ambiente Windows


## Instalação

Para criar o ambiente virtual
```bash
  python -m venv env
```

Em seguida, ative o ambiente
```bash
  .\env\Scripts\activate
```

Após ativado, instale as dependências em requirements.txt
```bash
  pip install -r requirements.txt
```

Realize as migrações pendentes
```bash
  python manage.py makemigrations
  python manage.py migrate
```

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

*Crie um arquivo com nome .env na raíz do projeto*

`SECRET_KEY` = SECRET_KEY = django-insecure-pko3bmgvvf^!j2f(#mx+9f+-v@y=z^rk8k4#rd=1hh!(1txfc6


Por fim, suba o servidor local
```bash
  python manage.py runserver
```
## Uso - Rotas

Rota: 
    (localhost:8000/api) - API Root DRF

Populando banco:
```bash
  python manage.py import_data
```

Realizando consulta:
```bash
  cd api/utils
  python test_client.py
```