# Django CRUD com Poetry

Bem-vindo ao projeto **Django CRUD**! Este projeto é um CRUD básico desenvolvido com **Django**, usando o **Django REST Framework** e gerenciado pelo **Poetry**. Ele foi projetado para demonstrar boas práticas de desenvolvimento backend e pode ser facilmente adaptado para projetos mais complexos.

---

## 🛠️ Tecnologias Utilizadas

- **Python ^3.11.11**
- **Django** ^5.1.4
- **Django REST Framework** ^3.15.2
- **Poetry** para gerenciamento de dependências
- **SQLite** (banco de dados padrão, mas você pode usar PostgreSQL ou outros)
- **Pytest** para aplicação de testes que validam as funcionalidades

---

## 🎯 Funcionalidades

- API RESTful para gerenciar um recurso de exemplo (`careers`).
- Funcionalidades completas de CRUD:
  - **Criar registros**
  - **Listar registros**
  - **Atualizar registros**
  - **Excluir registros**
- Sistema de paginação para endpoints.
- Fácil extensão para novos recursos e funcionalidades.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:
- **Python 3.8+**
- **Poetry**
- **Git** (para clonar o repositório)

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/usuario/seu-repositorio.git
   cd seu-repositorio
    ```
2. **Instale as dependências do projeto**
    ```bash
    poetry install
    ```
3. **Ative o ambiente virtual do Poetry**
    ```bash
    poetry shell
    ```
4. **Aplique as migrações do banco de dados**
    ```bash
    python backend/manage.py migrate
    ```
5. **Inicie o servidor de desenvolvimento**
    ```bash
    python backend/manage.py runserver
    ```
6. **Acesse o sistema no navegador em** http://127.0.0.1:8000/careers/. 

---
# Endpoints da API - Careers

Abaixo está a documentação dos endpoints disponíveis na API **Careers**.

## Base URL

http://127.0.0.1:8000/careers/

## Endpoints

### 1. **Listar Posts**
   - **URL:** `/careers/`
   - **Método:** `GET`
   - **Descrição:** Lista todos os posts com paginação.
   - **Resposta de Sucesso (200):**
     ```json
     {
         "count": 2,
         "next": null,
         "previous": null,
         "results": [
             {
                 "id": 1,
                 "username": "joao",
                 "created_datetime": "2024-12-13T10:00:00Z",
                 "title": "Primeiro Post",
                 "content": "Conteúdo do primeiro post"
             },
             {
                 "id": 2,
                 "username": "maria",
                 "created_datetime": "2024-12-13T10:05:00Z",
                 "title": "Segundo Post",
                 "content": "Conteúdo do segundo post"
             }
         ]
     }
     ```

---

### 2. **Criar Post**
   - **URL:** `/careers/`
   - **Método:** `POST`
   - **Descrição:** Cria um novo post.
   - **Corpo da Requisição:**
     ```json
     {
         "username": "joao",
         "title": "Novo Post",
         "content": "Conteúdo do novo post"
     }
     ```
   - **Resposta de Sucesso (201):**
     ```json
     {
         "id": 3,
         "username": "joao",
         "created_datetime": "2024-12-13T10:10:00Z",
         "title": "Novo Post",
         "content": "Conteúdo do novo post"
     }
     ```

---

### 3. **Detalhar Post**
   - **URL:** `/careers/{id}/`
   - **Método:** `GET`
   - **Descrição:** Recupera um post pelo ID.
   - **Resposta de Sucesso (200):**
     ```json
     {
         "id": 1,
         "username": "joao",
         "created_datetime": "2024-12-13T10:00:00Z",
         "title": "Primeiro Post",
         "content": "Conteúdo do primeiro post"
     }
     ```
   - **Resposta de Erro (404):**
     ```json
     {
         "detail": "Not found."
     }
     ```

---

### 4. **Atualizar Post**
   - **URL:** `/careers/{id}/`
   - **Método:** `PUT` ou `PATCH`
   - **Descrição:** Atualiza um post existente. (Campos `id`, `username` e `created_datetime` são imutáveis.)
   - **Corpo da Requisição:**
     ```json
     {
         "title": "Título Atualizado",
         "content": "Conteúdo Atualizado"
     }
     ```
   - **Resposta de Sucesso (200):**
     ```json
     {
         "id": 1,
         "username": "joao",
         "created_datetime": "2024-12-13T10:00:00Z",
         "title": "Título Atualizado",
         "content": "Conteúdo Atualizado"
     }
     ```
   - **Resposta de Erro (400):**
     ```json
     {
         "non_field_errors": ["Os campos 'id', 'username' e 'created_datetime' não podem ser alterados."]
     }
     ```

---

### 5. **Excluir Post**
   - **URL:** `/careers/{id}/`
   - **Método:** `DELETE`
   - **Descrição:** Exclui um post existente.
   - **Resposta de Sucesso (204):**
     Sem conteúdo.
   - **Resposta de Erro (404):**
     ```json
     {
         "detail": "Not found."
     }
     ```
