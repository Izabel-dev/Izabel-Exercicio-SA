 # 🛍️ IzabellaEstilo - Sistema de Gerenciamento

Sistema web desenvolvido com **Django** para gerenciamento de **produtos, categorias e pedidos**, incluindo autenticação de usuários, interface administrativa e API RESTful.

---

## 🚀 Funcionalidades

* 🔐 Autenticação de usuários (login e cadastro)
* 📦 Gerenciamento de Produtos (CRUD)
* 🗂️ Gerenciamento de Categorias (CRUD)
* 🧾 Gerenciamento de Pedidos (CRUD)
* 🌐 API RESTful com Django REST Framework
* 💬 Mensagens de feedback ao usuário
* 🔒 Controle de acesso com autenticação

---

## 📋 Requisitos do Projeto (SENAI)

* ✔ Página de login
* ✔ Pelo menos 3 páginas protegidas (Produtos, Categorias, Pedidos)
* ✔ 3 models distintos:

  * Categoria
  * Produto
  * Pedido
* ✔ CRUD completo via interface web
* ✔ CRUD completo via API
* ✔ Rotas separadas para API
* ✔ Feedback visual ao usuário

---

## ⚙️ Tecnologias Utilizadas

* Python
* Django
* Django REST Framework
* SQLite
* HTML, CSS (Bootstrap 5)
* JavaScript

---

## 🛠️ Instalação e Execução

### 1. Acesse o projeto

```bash
cd izabellaestilo_project
```

### 2. Crie o ambiente virtual

```bash
python3 -m venv venv
```

### 3. Ative o ambiente

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Aplique as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. (Opcional) Popular banco de dados

```bash
python seed.py
```

> Será criado:
>
> * Usuário: `admin`
> * Senha: `admin123`

### 8. Execute o servidor

```bash
python manage.py runserver
```

---

## 🌍 Acesso ao Sistema

### 🔗 Interface Web

* Home: `/`
* Login: `/login/`
* Cadastro: `/cadastro/`
* Produtos: `/produtos/` 🔒
* Categorias: `/categorias/` 🔒
* Pedidos: `/pedidos/` 🔒

---

### 🔧 Admin Django

Acesse:

```
http://127.0.0.1:8000/admin/
```

---

### 🔌 API REST

* Categorias: `/api/categorias/`
* Produtos: `/api/produtos/`
* Pedidos: `/api/pedidos/`

📌 Métodos suportados:

* GET
* POST
* PUT
* PATCH
* DELETE

📌 Permissões:

* Leitura pública (categorias/produtos)
* Escrita requer autenticação
* Pedidos: apenas usuários autenticados

---

## 📁 Estrutura do Projeto

```
izabellaestilo_project/
│
├── izabellaestilo/        # Configuração principal
├── core/                  # App principal
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   ├── serializers.py
│   └── urls.py
│
├── templates/
├── static/
├── manage.py
├── seed.py
└── requirements.txt
```

---

## 🔐 Segurança

* Rotas protegidas com `@login_required`
* API com permissões:

  * `IsAuthenticated`
  * `IsAuthenticatedOrReadOnly`
* Validação de formulários nativa do Django

---



    


