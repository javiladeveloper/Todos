from todolist import storage

def seed_data():
    storage.create({
        "title": "Aprender FastAPI",
        "description": "Estudiar la documentación oficial y hacer ejemplos.",
        "completed": False,
    })

    storage.create({
        "title": "Implementar ToDo API",
        "description": "Completar el reto técnico usando FastAPI.",
        "completed": True,
    })

    storage.create({
        "title": "Subir proyecto a GitHub",
        "description": "Publicar el código con README y Docker.",
        "completed": False,
    })
