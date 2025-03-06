# tests/test_task_storage.py
import unittest
import os
import json
from task_manager.task_storage import TaskStorage
from task_manager.task import Task, TaskStatus
import datetime

class TestTaskStorage(unittest.TestCase):

    def setUp(self):
        os.makedirs('/tmp/task_manager_tests', exist_ok=True)
        self.test_file = '/tmp/task_manager_tests/test_tasks.json'
        print(f'setUp: test_file path: {self.test_file}') # Debug print
        print(f'Current working directory: {os.getcwd()}') # Debug print - Current working directory
        self.task_storage = TaskStorage(self.test_file)

    def tearDown(self):
        print(f'tearDown: test_file path: {self.test_file}') # Debug print
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
            {"id": "task1", "title": "Task 1", "description": "Description 1", "due_date": None, "status": "Pending", "created_date": "2024-01-20"},
            {"id": "task2", "title": "Task 2", "description": "Description 2", "due_date": "2023-12-31", "status": "Completed", "created_date": "2024-01-20"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(tasks_data, f)

        tasks = self.task_storage.load_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, "task1")
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[0].description, "Description 1")
        self.assertEqual(tasks[0].due_date, None)
        self.assertEqual(tasks[0].status, TaskStatus.PENDING)
        self.assertEqual(tasks[1].id, "task2")
        self.assertEqual(tasks[1].title, "Task 2")
        self.assertEqual(tasks[1].description, "Description 2")
        self.assertEqual(tasks[1].due_date, datetime.date(2023, 12, 31))
        self.assertEqual(tasks[1].status, TaskStatus.COMPLETED)

    def test_save_tasks_empty_list(self):
        tasks = []
        self.task_storage.save_tasks(tasks)

        with open(self.test_file, 'r') as f:
            loaded_tasks_data = json.load(f)
        self.assertEqual(loaded_tasks_data, [])

    def test_save_tasks_non_empty_list(self):
        tasks = [
            Task("Task 1", "Description 1"), # Status defaults to PENDING (correct for Task 1)
            Task("Task 2", "Description 2", datetime.date(2024, 1, 1), 'medium', TaskStatus.COMPLETED) # Explicitly set status to COMPLETED and add priority
        ]
        self.task_storage.save_tasks(tasks)

        with open(self.test_file, 'r') as f:
            loaded_tasks_data = json.load(f)

        self.assertEqual(len(loaded_tasks_data), 2)
        self.assertEqual(loaded_tasks_data[0]['id'], tasks[0].id)
        self.assertEqual(loaded_tasks_data[0]['title'], "Task 1")
        self.assertEqual(loaded_tasks_data[0]['description'], "Description 1")
        self.assertEqual(loaded_tasks_data[0]['due_date'], None)
        self.assertEqual(loaded_tasks_data[0]['status'], 'Pending') # Assert status is 'Pending' for Task 1
        self.assertEqual(loaded_tasks_data[1]['id'], tasks[1].id)
        self.assertEqual(loaded_tasks_data[1]['title'], "Task 2")
        self.assertEqual(loaded_tasks_data[1]['description'], "Description 2")
        self.assertEqual(loaded_tasks_data[1]['due_date'], '2024-01-01')
        self.assertEqual(loaded_tasks_data[1]['status'], 'Completed') # Assert status is 'Completed' for Task 2

    def test_load_tasks_file_not_found(self):
        # Ensure the test file does not exist
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        # Load tasks, should handle file not found
        tasks = self.task_storage.load_tasks()

        # Assert that it returns an empty list or handles it appropriately
        self.assertEqual(tasks, [])
