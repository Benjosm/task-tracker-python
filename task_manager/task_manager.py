# task_manager/task_manager.py

import datetime
import json
import os
from task_manager.task import Task, TaskStatus
from task_manager.task_storage import TaskStorage


class TaskManager:
    """Manages task operations for the application."""

    def __init__(self, storage_path="tasks.json"):
        """Initialize the TaskManager with a storage path.

        Args:
            storage_path (str): Path to the task storage file.
        """
        self.storage = TaskStorage(storage_path)
        self.tasks = self.storage.load_tasks()

    def clear_tasks(self):
        """Clears all tasks from the task list and storage."""
        self.tasks = []
        self.storage.save_tasks([])

    def add_task(self, title, description="", due_date=None, priority="medium"):
        """Add a new task to the task list.

        Args:
            title (str): Task title
            description (str, optional): Task description. Defaults to empty string.
            due_date (str, optional): Due date in format YYYY-MM-DD. Defaults to None.
            priority (str, optional): Task priority (low, medium, high). Defaults to "medium".

        Returns:
            Task: The newly created task object
        """
        if not title:
            raise ValueError("Task title cannot be empty.")
        if len(title) > 100:
            raise ValueError("Task title is too long. Maximum length is 100 characters.")
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be one of 'low', 'medium', 'high'")
        if due_date:
            try:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Due date must be in the format YYYY-MM-DD")

        task = Task(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority
        )
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return task

    def list_tasks(self, show_completed=False):
        """List all tasks, with option to include or exclude completed tasks.

        Args:
            show_completed (bool, optional): Whether to include completed tasks. Defaults to False.

        Returns:
            list: List of tasks matching the criteria
        """
        if show_completed:
            return self.tasks
        return [task for task in self.tasks if task.status != TaskStatus.COMPLETED]

    def complete_task(self, task_id):
        """Mark a task as completed.

        Args:
            task_id (str): The ID of the task to mark as completed

        Returns:
            bool: True if the task was found and marked as completed, False otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                task.status = TaskStatus.COMPLETED
                task.completed_date = datetime.date.today()
                self.storage.save_tasks(self.tasks)
                return True
        return False

    def delete_task(self, task_id):
        """Delete a task.

        Args:
            task_id (str): The ID of the task to delete

        Returns:
            bool: True if the task was found and deleted, False otherwise
        """
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
                self.storage.save_tasks(self.tasks)
                return True
        return False

    def get_task_by_id(self, task_id):
        """Find a task by its ID.

        Args:
            task_id (str): The ID of the task to find

        Returns:
            Task: The task with the matching ID, or None if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_statistics(self):
        """Get statistics about tasks.

        Returns:
            dict: Dictionary with task statistics
        """
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.status == TaskStatus.COMPLETED)
        pending = total - completed
        
        priorities = {"low": 0, "medium": 0, "high": 0}
        for task in self.tasks:
            if task.priority in priorities:
                priorities[task.priority] += 1
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "priorities": priorities
        }

    def edit_task(self, task_id, title=None, description=None, due_date=None, priority=None):
        """Edit an existing task.

        Args:
            task_id (str): The ID of the task to edit
            title (str, optional): New title for the task. Defaults to None.
            description (str, optional): New description for the task. Defaults to None.
            due_date (str, optional): New due date in format YYYY-MM-DD. Defaults to None.
            priority (str, optional): New priority (low, medium, high). Defaults to None.

        Returns:
            bool: True if the task was found and edited, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID '{task_id}' not found.")
        if title is not None:
            if not title:
                raise ValueError("Task title cannot be empty.")
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            try:
                task.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
            except ValueError:
                raise ValueError("Due date must be in the format YYYY-MM-DD")
        if priority is not None:
            task.priority = priority
        self.storage.save_tasks(self.tasks)
        return True
