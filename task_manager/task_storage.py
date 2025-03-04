"""
Task storage module for the Task Manager application.

Handles saving and loading tasks from a JSON file.
"""
import json
import os
from .task import Task


class TaskEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Task):
            return obj.to_dict()
        return super().default(obj)


class TaskStorage:
    """Handles persistence of tasks to and from storage."""

    def __init__(self, storage_path="tasks.json"):
        """Initialize TaskStorage with a path to the storage file."""
        self.storage_path = storage_path

    def save_tasks(self, tasks):
        """Save tasks to the storage file."""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)  # Ensure directory exists
        with open(self.storage_path, 'w') as f:
            json.dump(tasks, f, indent=4, cls=TaskEncoder)

    def load_tasks(self):
        """Load tasks from the storage file."""
        if not os.path.exists(self.storage_path):
            return []  # Return empty list if file doesn't exist
        try:
            with open(self.storage_path, 'r') as f:
                task_data_list = json.load(f)
                tasks = [Task.from_dict(task_data) for task_data in task_data_list]
                return tasks
        except json.JSONDecodeError:
            return []  # Return empty list if JSON is invalid
