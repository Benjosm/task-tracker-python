"""
Task class module for the Task Manager application.

This module defines the Task class which represents a single task
with properties like title, description, due date, etc.
"""
import datetime
import uuid


class Task:
    """Represents a single task in the task management system."""

    def __init__(self, title, description="", due_date=None, priority="medium"):
        """Initialize a new Task.

        Args:
            title (str): The title of the task
            description (str, optional): Description of the task. Defaults to "".
            due_date (datetime.date, optional): Due date of the task. Defaults to None.
            priority (str, optional): Priority level (low, medium, high). Defaults to "medium".
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.created_date = datetime.date.today()
        self.completed = False
        self.completed_date = None

    def to_dict(self):
        """Convert the task to a dictionary for storage.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "priority": self.priority,
            "created_date": self.created_date.isoformat(),
            "completed": self.completed,
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
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", "medium")
        )
        
        task.id = data["id"]
        
        if data.get("due_date"):
            task.due_date = datetime.date.fromisoformat(data["due_date"])
            
        task.created_date = datetime.date.fromisoformat(data["created_date"])
        task.completed = data.get("completed", False)
        
        if data.get("completed_date"):
            task.completed_date = datetime.date.fromisoformat(data["completed_date"])
            
        return task

    def __str__(self):
        """String representation of the task.

        Returns:
            str: String representation
        """
        status = "Completed" if self.completed else "Pending"
        due = f"Due: {self.due_date}" if self.due_date else "No due date"
        return f"{self.title} ({status}) - {due} - Priority: {self.priority}"
