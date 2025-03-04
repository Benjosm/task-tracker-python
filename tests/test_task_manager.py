import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_manager.task import Task
from task_manager.task_manager import TaskManager
import pytest


def test_add_task_priority():
    manager = TaskManager()
    task = Task("Test Task", description="", priority="High")
    print(f"Task priority after creation: {task.priority}") # Debug print
    manager.add_task(task)
    print(f"Task priority after adding to manager: {manager.tasks[0].priority if manager.tasks else None}") # Debug print
    assert len(manager.tasks) == 1
    assert manager.tasks[0].priority == "High"


def test_add_task_priority_fail():
    manager = TaskManager()
    task = Task("Test Task", description="", priority="Medium")
    manager.add_task(task)
    assert manager.tasks[0].priority == "Medium"