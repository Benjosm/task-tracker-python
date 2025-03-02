from __future__ import annotations
from typing import List
from task_manager.task import Task


class TaskManager:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def complete_task(self, task: Task) -> None:
        pass

    def delete_task(self, task: Task) -> None:
        pass

    def get_all_tasks(self) -> List[Task]:
        return self.tasks