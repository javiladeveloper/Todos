from app.infrastructure.in_memory_repo import InMemoryTaskRepo


def seed_data(repo: InMemoryTaskRepo) -> None:

    if repo.get_all():
        return

    repo.create(
        {
            "title": "Aprender FastAPI",
            "description": "Estudiar la documentación oficial y hacer ejemplos.",
            "completed": False,
        }
    )

    repo.create(
        {
            "title": "Completar reto técnico",
            "description": "Terminar API REST + GraphQL con buenas prácticas.",
            "completed": True,
        }
    )

    repo.create(
        {
            "title": "Publicar en GitHub",
            "description": "Subir proyecto con README y Docker.",
            "completed": False,
        }
    )

    repo.create(
        {
            "title": "Documentar API",
            "description": "Escribir cómo funciona cada endpoint y cómo correr los tests.",
            "completed": False,
        }
    )

    repo.create(
        {
            "title": "Mejorar cobertura de tests",
            "description": "Agregar más pruebas unitarias y de integración.",
            "completed": False,
        }
    )

    repo.create(
        {
            "title": "Preparar demo para revisión",
            "description": "Practicar explicación del código y decisiones tomadas.",
            "completed": True,
        }
    )

    repo.create(
        {
            "title": "Refactorizar el servicio",
            "description": "Separar validaciones y aplicar principios SOLID.",
            "completed": False,
        }
    )

    repo.create(
        {
            "title": "Agregar GraphQL mutations",
            "description": "Permitir crear y actualizar tareas desde el playground.",
            "completed": False,
        }
    )

    repo.create(
        {
            "title": "Deploy en Render",
            "description": "Subir la app como servicio gratuito para mostrarla.",
            "completed": False,
        }
    )

    repo.create(
        {
            "title": "Presentar solución al equipo",
            "description": "Compartir pantalla y explicar diseño de la API.",
            "completed": False,
        }
    )
