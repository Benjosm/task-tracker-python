# task_manager/task.py


"""
Task class module for the Task Manager application.

This module defines the Task class which represents a single task
with properties like title, description, due date, etc.
"""
import datetime
import uuid
from enum import Enum

class TaskStatus(Enum):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'


class Task:
    """Represents a single task in the task management system."""

    def __init__(self, title, description="", due_date=None, priority='medium', status=TaskStatus.PENDING):
        """Initialize a new Task.

        Args:
            title (str): The title of the task
            description (str, optional): Description of the task. Defaults to "".
            due_date (datetime.date, optional): Due date of the task. Defaults to None.
            priority (str, optional): Priority level (low, medium, high). Defaults to 'medium'.
            status (TaskStatus, optional): Status of the task. Defaults to TaskStatus.PENDING.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.created_date = datetime.date.today()
        self.status = status  # Use the provided status, or default to PENDING
        self.completed_date = None

    def to_dict(self):
        """Convert the task to a dictionary for storage.

        Returns:
            dict: Dictionary representation of the task
        """
        print(f'DEBUG to_dict: self.due_date = {self.due_date}, type(self.due_date) = {type(self.due_date)}')
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat() if isinstance(self.due_date, datetime.date) else None,
            "priority": str(self.priority.value) if isinstance(self.priority, TaskStatus) else str(self.priority) if isinstance(self.priority, Enum) else self.priority,
            "created_date": self.created_date.isoformat(),
            "status": str(self.status.value),
            "completed_date": self.completed_date.isoformat() if self.completed_date else None
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from a dictionary.

        Args:
            data (dict): Dictionary containing task data

        Returns:
            Task: A new Task object
        """
        print(f'DEBUG from_dict: data = {data}')
        task = cls(
            title=data['title'],
            description=data.get("description", ""),
            priority=data.get("priority", "medium"),
            status=TaskStatus(data.get('status', 'Pending')) # Load status from value, default to PENDING
        )

        task.id = data['id']

        if data.get("due_date"):
            task.due_date = datetime.date.fromisoformat(data["due_date"])

        task.created_date = datetime.date.fromisoformat(data["created_date"])

        if data.get("completed_date"):
            task.completed_date = datetime.date.fromisoformat(data["completed_date"])

        return task

    def __str__(self):
        """String representation of the task.

        Returns:
            str: String representation
        """
        due = f"Due: {self.due_date}" if self.due_date else "No due date"
        return f"{self.title} ({self.status.value}) - {due} - Priority: {self.priority}" # Use status value
