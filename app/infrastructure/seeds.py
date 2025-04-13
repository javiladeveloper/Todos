from app.domain.entities import Task
from app.infrastructure.in_memory_repo import AbstractTaskRepository


def seed_data(repo: AbstractTaskRepository) -> None:
    if repo.list_tasks():
        return

    repo.create_task(
        Task(
            title="Aprender FastAPI",
            description="Estudiar la documentación oficial y hacer ejemplos.",
            completed=False,
        )
    )

    repo.create_task(
        Task(
            title="Completar reto técnico",
            description="Terminar API REST + GraphQL con buenas prácticas.",
            completed=True,
        )
    )

    repo.create_task(
        Task(
            title="Publicar en GitHub",
            description="Subir proyecto con README y Docker.",
            completed=False,
        )
    )

    repo.create_task(
        Task(
            title="Documentar API",
            description="Escribir cómo funciona cada endpoint y cómo correr los tests.",
            completed=False,
        )
    )

    repo.create_task(
        Task(
            title="Mejorar cobertura de tests",
            description="Agregar más pruebas unitarias y de integración.",
            completed=False,
        )
    )

    repo.create_task(
        Task(
            title="Preparar demo para revisión",
            description="Practicar explicación del código y decisiones tomadas.",
            completed=True,
        )
    )

    repo.create_task(
        Task(
            title="Refactorizar el servicio",
            description="Separar validaciones y aplicar principios SOLID.",
            completed=False,
        )
    )

    repo.create_task(
        Task(
            title="Agregar GraphQL mutations",
            description="Permitir crear y actualizar tareas desde el playground.",
            completed=False,
        )
    )

    repo.create_task(
        Task(
            title="Deploy en Render",
            description="Subir la app como servicio gratuito para mostrarla.",
            completed=False,
        )
    )

    repo.create_task(
        Task(
            title="Presentar solución al equipo",
            description="Compartir pantalla y explicar diseño de la API.",
            completed=False,
        )
    )
