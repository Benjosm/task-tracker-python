"""
Task storage module for the Task Manager application.

Handles saving and loading tasks from a JSON file.
"""
import json
import os
from .task import Task


class TaskStorage:
    """Handles persistence of tasks to and from storage."""

    def __init__(self, storage_path):
        """Initialize the storage with a file path.

        Args:
            storage_path (str): Path to the task storage file
        """
        self.storage_path = storage_path

    def save_tasks(self, tasks):
        """Save the tasks to the storage file.

        Args:
            tasks (list): List of Task objects to save
        """
        tasks_data = [task.to_dict() for task in tasks]
        with open(self.storage_path, 'w') as file:
            json.dump(tasks_data, file, indent=2)

    def load_tasks(self):
        """Load tasks from the storage file.

        Returns:
            list: List of Task objects
        """
        if not os.path.exists(self.storage_path):
            return []
        
        try:
            with open(self.storage_path, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(task_data) for task_data in tasks_data]
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is empty or corrupted, return empty list
            return []
