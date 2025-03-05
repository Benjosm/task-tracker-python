import pytest
from task_manager.task import Task
from task_manager.task import TaskStatus


def test_task_creation():
    task = Task("Test Task", "This is a test task", TaskStatus.PENDING)
    assert task is not None
    assert task.title == "Test Task"
    assert task.description == "This is a test task"
    assert task.status == TaskStatus.PENDING

def test_task_status_enum():
    assert TaskStatus.PENDING == 'PENDING'
    assert TaskStatus.IN_PROGRESS == 'IN_PROGRESS'
    assert TaskStatus.COMPLETED == 'COMPLETED'
