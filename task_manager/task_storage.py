# task_manager/task_storage.py
import json
import os
import traceback
from task_manager.task import Task

class TaskStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_tasks(self, tasks):
        tasks_data = [task.to_dict() for task in tasks]
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w') as file:
                json.dump(tasks_data, file, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        print(f"Type of self.file_path in load_tasks: {type(self.file_path)}")
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
            return [Task.from_dict(task_data) for task_data in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
