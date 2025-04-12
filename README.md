# ToDo List API

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)
[![CI](https://github.com/javiladeveloper/Todos/actions/workflows/ci.yml/badge.svg)](https://github.com/javiladeveloper/Todos/actions/workflows/ci.yml)


Este proyecto es una API RESTful y GraphQL construida con FastAPI para gestionar tareas (ToDo List). Fue desarrollado como parte de un reto técnico con enfoque profesional, aplicando Clean Architecture, principios SOLID, validaciones robustas, logging estructurado, paginación, entorno multilenguaje y control por entorno.

---

## 🧩 Descripción del proyecto

Permite crear, listar, actualizar y eliminar tareas. Cada tarea incluye un título, una descripción opcional, un estado de completado y un identificador único.

### 📦 Ejemplo de tarea

```json
{
  "id": 1,
  "title": "Estudiar FastAPI",
  "description": "Leer la documentación oficial",
  "completed": false
}

```

---

## Cómo correr el proyecto localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/javiladeveloper/Todos.git
cd Todos 
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # En Windows
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```
### 4. Configurar variables de entorno
Crea un archivo .env con:
```ini
ENV=dev
```
Y uno adicional .env.dev con:
```ini
LOG_LEVEL=DEBUG
LANG=es
API_VERSION_PATH=v1
ENABLE_GRAPHQL=true
API_TITLE=ToDo API
API_VERSION=1.0.0
API_DESCRIPTION=API RESTful y GraphQL para gestionar tareas.
API_CONTACT_NAME=Javila Developer
API_CONTACT_URL=https://github.com/javiladeveloper
API_CONTACT_EMAIL=jonathan.joan.avila@gmail.comexample.com

```

### 5. Levantar la app

```bash
uvicorn todolist.main:app --reload
```

Podés acceder a la documentación interactiva en:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

---

## Usar Docker (opcional)

### Opción 1: build + run

```bash
docker build -t todo-api .
docker run -p 8000:8000 todo-api
```

### Opción 2: usando docker-compose

```bash
docker-compose up --build
```

Esto levantará la app y podrás acceder a:

- REST API: [http://localhost:8000/docs](http://localhost:8000/docs)
- GraphQL: [http://localhost:8000/graphql](http://localhost:8000/graphql)

---

## Correr pruebas

Asegurate de tener el entorno virtual activado y corré:

```bash
pytest
```

También podés ejecutar por separado:

```bash
pytest tests/test_services.py 
pytest tests/test_e2e.py  
```

> Las pruebas usan una lista en memoria, así que el estado se reinicia cada vez que se ejecutan.

---

## Herramientas utilizadas

- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Black & Flake8
- Docker
- Pre-commit
- httpx (para pruebas E2E)
- Strawberry (para GraphQL)
- logging (para trazabilidad)
- Soporte multiidioma (LANG=es|en)

---

## Estructura del proyecto

```
.
.
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── routes/
│   │       │   ├── task_routes.py
│   │       │   └── system_routes.py
│   │       └── dependencies.py
│   ├── config.py
│   ├── core/
│   │   ├── exceptions.py
│   │   ├── logger.py
│   │   └── openapi.py
│   ├── domain/
│   │   ├── entities.py
│   │   └── schemas.py
│   ├── docs/
│   │   └── openapi_tags.py
│   ├── graphql/
│   │   ├── resolvers.py
│   │   ├── schema.py
│   │   └── types.py
│   ├── infrastructure/
│   │   ├── interfaces.py
│   │   ├── in_memory_repo.py
│   │   ├── repo_instance.py
│   │   └── seeds.py
│   ├── services/
│   │   └── task_service.py
│   └── main.py
├── tests/
│   ├── unit/
│   └── e2e/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env / .env.dev / .env.prod
└── README.md
```

---

## Extras

- Middleware de logging para errores no controlados.
- Control total de errores con ExceptionHandlers personalizados.
- Validaciones con Pydantic (validator, root_validator).
- Paginación y manejo de límites.
- Soporte multilenguaje en documentación OpenAPI.

---

## Interfaz GraphQL (Bonus)

Además de la API RESTful, este proyecto incluye una interfaz alternativa en GraphQL usando [Strawberry](https://strawberry.rocks/).

### 📌 Endpoint

- GraphQL Playground: [http://localhost:8000/graphql](http://localhost:8000/graphql)

> Desde ahí podés ejecutar queries y mutations directamente desde el navegador.

---

### 📋 Ejemplo de Query

```graphql
query {
  tasks {
    id
    title
    completed
  }
}
```

---

### ✏️ Ejemplo de Mutation

```graphql
mutation {
  createTask(
    title: "Tarea desde GraphQL"
    description: "Creada desde el playground"
    completed: false
  ) {
    id
    title
    completed
  }
}
```

---

Esta interfaz permite consultar y modificar tareas utilizando GraphQL como una alternativa moderna y flexible a los endpoints REST.

