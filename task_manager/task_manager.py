"""
Task Manager - A simple command-line task management application
"""
from .task_storage import TaskStorage
from .task import Task

class TaskManager:
    """Manages task operations for the application."""

    def __init__(self, storage_path="tasks.json"): # Removed type hinting for simplicity
        """Initialize the TaskManager with a storage path."""
        self.storage = TaskStorage(storage_path)
        self.tasks = [] # In-memory task storage for now

    def add_task(self, task: Task): # Added type hinting
        """Adds a task to the task list."""
        self.tasks.append(task)

    def list_tasks(self): # keep a simple function to see if import works
        return self.tasks
