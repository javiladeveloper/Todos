from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    title: str
    description: str
    completed: bool
    id: Optional[int] = field(default=None)
