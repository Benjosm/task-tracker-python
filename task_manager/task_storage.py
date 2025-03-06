# task_manager/task_storage.py
import json
import os
import traceback
from task_manager.task import Task

class TaskStorage:
    def __init__(self, file_path):
        print(f"TaskStorage.__init__: file_path: {file_path}") # ADD THIS LINE
        self.file_path = file_path

    def save_tasks(self, tasks):
        tasks_data = [task.to_dict() for task in tasks]
        try:
            print(f"self.file_path in save_tasks: {self.file_path}") # ADD THIS LINE
            if self.file_path != ':memory:':
                os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
                with open(self.file_path, 'w') as file:
                    json.dump(tasks_data, file, indent=2)
            else:
                print("Skipping file operations for :memory: storage")
        except OSError as e:
            if e.errno in [13, 30]:  # errno 13: Permission denied, errno 30: Read-only file system
                raise PermissionError(f"Permission error saving tasks to {self.file_path}: {e}") from e
            else:
                raise  # Re-raise other OS errors
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        print(f"Type of self.file_path in load_tasks: {type(self.file_path)}")
        if not os.path.exists(self.file_path) or self.file_path == ':memory:':
            return []
        try:
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
            return [Task.from_dict(task_data) for task_data in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
