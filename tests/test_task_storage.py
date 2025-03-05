# tests/test_task_storage.py
import unittest
import os
import json
from task_manager.task_storage import TaskStorage
from task_manager.task import Task

class TestTaskStorage(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_tasks.json'
        self.task_storage = TaskStorage(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_tasks_empty_file(self):
        # Create an empty test file
        with open(self.test_file, 'w') as f:
            json.dump([], f)

        tasks = self.task_storage.load_tasks()
        self.assertEqual(tasks, [])

    def test_load_tasks_non_empty_file(self):
        # Create a test file with some tasks
        tasks_data = [
            {"description": "Task 1", "due_date": None, "complete": False},
            {"description": "Task 2", "due_date": "2023-12-31", "complete": True}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(tasks_data, f)

        tasks = self.task_storage.load_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].description, "Task 1")
        self.assertEqual(tasks[0].due_date, None)
        self.assertEqual(tasks[0].complete, False)
        self.assertEqual(tasks[1].description, "Task 2")
        self.assertEqual(tasks[1].due_date, "2023-12-31")
        self.assertEqual(tasks[1].complete, True)

    def test_save_tasks_empty_list(self):
        tasks = []
        self.task_storage.save_tasks(tasks)

        with open(self.test_file, 'r') as f:
            loaded_tasks_data = json.load(f)
        self.assertEqual(loaded_tasks_data, [])

    def test_save_tasks_non_empty_list(self):
        tasks = [
            Task("Task 1"),
            Task("Task 2", "2024-01-01", True)
        ]
        self.task_storage.save_tasks(tasks)

        with open(self.test_file, 'r') as f:
            loaded_tasks_data = json.load(f)

        self.assertEqual(len(loaded_tasks_data), 2)
        self.assertEqual(loaded_tasks_data[0]['description'], "Task 1")
        self.assertEqual(loaded_tasks_data[0]['due_date'], None)
        self.assertEqual(loaded_tasks_data[0]['complete'], False)
        self.assertEqual(loaded_tasks_data[1]['description'], "Task 2")
        self.assertEqual(loaded_tasks_data[1]['due_date'], "2024-01-01")
        self.assertEqual(loaded_tasks_data[1]['complete'], True)