# /tests/test_task_manager_add_task.py

import tempfile
import os
from task_manager.task_manager import TaskManager
from task_manager.task_storage import TaskStorage


def test_add_task():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        task_storage = TaskStorage(tmp_file.name)
        task_manager = TaskManager(tmp_file.name) # Corrected: Pass file path string
        task_manager.add_task("Test Task", priority="High")
        tasks = task_manager.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Test Task"  # Changed 'name' to 'title'
        assert tasks[0].priority == "High"
    os.unlink(tmp_file.name)