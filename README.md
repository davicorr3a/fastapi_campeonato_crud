# Sistema de Gerenciamento de Campeonato de Futebol - UFS

Projeto desenvolvido como parte da disciplina de **Banco de Dados** da Universidade Federal de Sergipe (UFS), com o objetivo de aplicar os conceitos de bancos de dados relacionais e não relacionais de forma integrada e prática.

## Sobre o Projeto

Este sistema permite o gerenciamento completo de um campeonato de futebol, incluindo:

- Criação e edição de **Ligas**, **Times**, **Estádios** e **Partidas**
- Armazenamento dos dados em **PostgreSQL** (relacional) e **MongoDB** (não relacional)
- Interface web interativa feita com **FastAPI** e **Jinja2 Templates**
- Separação clara entre as opções relacionais e não relacionais

## Integrantes
- Davi de Andrade Corrêa
- Matheus Vinícius

## Tecnologias Utilizadas
- Python 3.12
- FastAPI
- PostgreSQL
- MongoDB (MongoDB Atlas)
- Bootstrap 5
- Jinja2

## Funcionalidades

### Banco Relacional (PostgreSQL)
- CRUD de Ligas
- CRUD de Times (com liga associada)
- CRUD de Estádios
- CRUD de Partidas (com times e estádios relacionados)

### Banco Não Relacional (MongoDB)
- CRUD de Ligas
- CRUD de Times (com liga por nome)
- CRUD de Estádios
- CRUD de Partidas (com nomes de times e estádios)

## Como Usar a Ferramenta

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/fastapi_campeonato_crud.git
cd fastapi_campeonato_crud
```

### 2. Instale as dependências
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Configure o banco de dados
- **PostgreSQL**: Altere os dados de conexão em `postgres_crud.py`
- **MongoDB**: Insira sua URI diretamente em `mongo_crud.py`

### 4. Rode o projeto
```bash
uvicorn app.main:app --reload
```

### 5. Acesse pelo navegador
```
http://127.0.0.1:8000
```

### 6. Interaja com a aplicação
- Clique em **Banco Relacional** para usar o PostgreSQL
- Clique em **Banco Não Relacional** para usar o MongoDB
- A partir disso, é possível manipular todas as tabelas.

## Materiais de Apoio

Esses recursos podem ajudar a entender melhor os conceitos e ferramentas usadas no projeto:

- [FastAPI](https://www.datacamp.com/pt/tutorial/introduction-fastapi-tutorial)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MongoDB](https://www.alura.com.br/artigos/mongodb)
- [MongoDB Atlas - Guia](https://www.mongodb.com/cloud/atlas)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Uvicorn](https://www.uvicorn.org/)

## Objetivos Acadêmicos Atendidos

- Compreensão da diferença entre bancos relacionais e não relacionais
- Implementação de CRUDs com FastAPI
- Conexão simultânea com dois tipos de banco
- Interface web organizada e funcional

## Conclusão

Esse projeto proporcionou uma experiência prática em conceitos de Banco de Dados, integração com APIs, e desenvolvimento de uma interface funcional para o usuário final.

---

Se desejar contribuir ou melhorar este projeto, fique à vontade para abrir um PR.
