import pytest
from task_manager.task_manager import TaskManager


def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Test Task", "Test Description")
    assert task is not None
    assert task.title == "Test Task"
    assert task.description == "Test Description"


def test_get_task_by_id():
    manager = TaskManager()
    task1 = manager.add_task("Task 1", "Description 1")
    task2 = manager.add_task("Task 2", "Description 2")

    retrieved_task1 = manager.get_task_by_id(task1.id)
    assert retrieved_task1 is not None
    assert retrieved_task1.id == task1.id
    assert retrieved_task1.title == "Task 1"
    assert retrieved_task1.description == "Description 1"

    retrieved_task2 = manager.get_task_by_id(task2.id)
    assert retrieved_task2 is not None
    assert retrieved_task2.id == task2.id
    assert retrieved_task2.title == "Task 2"
    assert retrieved_task2.description == "Description 2"

    retrieved_task_none = manager.get_task_by_id("non_existent_id")
    assert retrieved_task_none is None