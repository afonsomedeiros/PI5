# Projeto Integrador 5.

## 1. Definições do backend.

Backend do projeto será desenvolvido utilizando python 3.x e utilizará mongodb para armazenamento.

### 1.1. Detalhamento Tecnológico.

Projeto será desenvolvido utilizando o micro-framework Flask para o serviço web, para servidor utilizaremos a vercel por oferecer suporte a python e possuir um serviço gratuito e a conexão com a base de dados será feita através do módulo pymongo.

### 1.2. Arquitetura do projeto.

A arquitetura planejada do projeto antes do inicio do desenvolvimento conterá a seguinte estrutura:

```sh
<ROOT_PATH>
├── api
│   ├── __init__.py
│   ├── controllers
│   │   └── __init__.py
│   ├── extensions
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   └── routes
│       └── __init__.py
├── application.py
├── data
│   └── __init__.py
└── server.py
```

Até a finalização do projeto é possível que seja alterada arquitetura afim de se adaptar melhor ao projeto.

### 1.3. Estreturação dos documentos.

existiram inicialmente 2 documentos essenciais: users e admeasurement.

users
```json
{
  'code': int,
  'name': string
  'email': string
  'password': string
}

```

admeasurement.
```
{
  "code": "int",
  "device_id": "int"
  "value": "float",
  "collected_at": "string"
}
```

### 1.4. Lista de endpoints.

POST
- [ ] `/user/auth` Autenticação do usuário.
Request
```json
{
  "email": "teste@teste.com",
  "password": "123456"
}
```
Response
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDI4MjMwMywianRpIjoiODMwYjY2YTQtNTJmMy00NjM3LTkxNzEtYjY0NTk0YzhkYzgwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjM0MjgyMzAzLCJleHAiOjE2MzQyODMyMDN9.g94zTPJ7OH48OagLtikjUHZkdWlKqPzMcksxs1UEDeQ",
    "message": "Login succefull!",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDI4MjMwMywianRpIjoiOWYzYjhjNWUtNDg1Yy00NjBmLTk3MmYtNjRlNmI1MzI1Mzc2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjEsIm5iZiI6MTYzNDI4MjMwMywiZXhwIjoxNjM2ODc0MzAzfQ.Qo_2yl1ZM56oh19qflQ8cSExPiPOO5UpkECxMS5aU8A"
}```

- [ ] `/admeasurement/new` Criação de nova medição.
Request
```
{
  "variable_id": "int",
  "value": "float",
  "date": "timestamp"
}
```
Response.
...

GET
- [ ] `/admeasurement[?device_id=0&between=yyyy-mm-dd,yyyy-mm-dd]` Retorna lista de medições e podeser filtrado por dispositivo e período.
```json
[
  {
    "code": "int"
    "variable_id": "int":
    "value": "float",
    "date": "timestamp"
  }
]
```
