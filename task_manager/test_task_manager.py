import pytest
from task_manager.task_manager import TaskManager
from task_manager.task import Task
import datetime



def test_add_task_fails():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task(title="Test Task", due_date="invalid-date")



def test_add_task_success():
    manager = TaskManager()
    task = manager.add_task(title="Test Task", due_date="2024-12-31")
    assert isinstance(task, Task)
    assert task.title == "Test Task"
    assert task.due_date == datetime.date(2024, 12, 31)
