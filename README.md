# ToDo List API

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

Este proyecto es una API RESTful desarrollada con FastAPI para gestionar tareas (ToDo List). Es parte de un reto técnico y está enfocada en mantener una estructura limpia, seguir buenas prácticas y usar herramientas comunes como Docker, pytest, black y flake8.

---


## Descripción del proyecto

La API permite crear, consultar, actualizar y eliminar tareas simples. Cada tarea contiene un título, una descripción opcional, un estado de completado y un ID único.

### Formato de una tarea

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
git clone <REPO_URL>
cd reto-tecnico-todolist
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

### 4. Levantar la app

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
- Black
- Flake8
- Docker
- httpx (para pruebas E2E)
- Strawberry (para GraphQL)
- logging (para trazabilidad)

---

## Estructura del proyecto

```
.
├── todolist/
│   ├── __init__.py          # expone solo lo necesario (router, storage, seed_data)
│   ├── main.py              # inicializa FastAPI + rutas
│   ├── routes.py            # define endpoints REST
│   ├── schemas.py           # modelos Pydantic para la API REST
│   ├── services.py          # lógica de negocio
│   ├── storage.py           # almacenamiento en memoria
│   ├── seed.py              # tareas dummy iniciales
│   ├── graphql.py           # esquema unificado (schema) para GraphQL
│   └── graphql_types.py     # tipos y resolvers GraphQL (Strawberry)
├── tests/
│   ├── __init__.py
│   ├── test_services.py     # pruebas unitarias
│   └── test_e2e.py          # pruebas end-to-end
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .flake8
├── pytest.ini
└── README.md
```

---

## Extras

- El archivo `__init__.py` en `todolist/` expone solo lo esencial: `storage`, `router`, `seed_data()`.
- Los modelos de datos para REST están en `schemas.py`, y los de GraphQL en `graphql_types.py`, manteniendo las capas desacopladas.
- Se usa `logging` para registrar eventos clave como errores 404.
- Las validaciones con Pydantic evitan que se creen tareas sin título o con descripciones demasiado largas.

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
