from task_manager.task_manager import TaskManager
from task_manager.task import Task

def test_add_task():
    manager = TaskManager()
    task = Task(description="Test Task")
    manager.add_task(task)
    tasks = manager.list_tasks()
    assert task in tasks