# This is a test comment to trigger a pull request.

from task_manager.task_storage import TaskStorage
from task_manager.task import Task
import datetime

class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage

    def add_task(self, summary: str, description: str, due_date: str = None, priority: str = None) -> Task:
        """Adds a new task to the task manager.
        Args:
            summary (str): The summary of the task.
            description (str): The description of the task.
            due_date (str, optional): The due date of the task in YYYY-MM-DD format. Defaults to None.
            priority (str, optional): The priority of the task. Defaults to None.
        Returns:
            Task: The created task.
        """
        try:
            if due_date:
                # Convert due_date to datetime object
                due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
            task = Task(summary=summary, description=description, due_date=due_date, priority=priority)
            self.storage.add_task(task)
            return task
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def get_task(self, task_id: int) -> Task:
        """Gets a task by its ID.
        Args:
            task_id (int): The ID of the task.
        Returns:
            Task: The task with the given ID, or None if not found.
        """
        return self.storage.get_task(task_id)

    def update_task(self, task_id: int, summary: str = None, description: str = None, due_date: str = None, priority: str = None, status: str = None) -> Task:
        """Updates an existing task.
        Args:
            task_id (int): The ID of the task to update.
            summary (str, optional): The new summary. Defaults to None.
            description (str, optional): The new description. Defaults to None.
            due_date (str, optional): The new due date in YYYY-MM-DD format. Defaults to None.
            priority (str, optional): The new priority. Defaults to None.
            status (str, optional): The new status. Defaults to None.
        Returns:
            Task: The updated task, or None if the task was not found.
        """
        task = self.get_task(task_id)
        if not task:
            return None
        try:
            if due_date:
                due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
            if summary is not None:
                task.summary = summary
            if description is not None:
                task.description = description
            if due_date is not None:
                task.due_date = due_date
            if priority is not None:
                task.priority = priority
            if status is not None:
                task.status = status
            self.storage.update_task(task)
            return task
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task.
        Args:
            task_id (int): The ID of the task to delete.
        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        return self.storage.delete_task(task_id)

    def list_tasks(self):
        """Lists all tasks.
        Returns:
            list: A list of all tasks.
        """
        return self.storage.list_tasks()

