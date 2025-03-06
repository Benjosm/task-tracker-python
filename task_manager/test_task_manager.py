# task_manager/test_task_manager.py

import unittest
from task_manager.task_manager import TaskManager
from task_manager.task import TaskStatus

class TestTaskManager(unittest.TestCase):

    def setUp(self): # setup method to create TaskManager instance before each test
        self.task_manager = TaskManager()
        self.task_manager.clear_tasks()

    def test_add_task(self):
        task = self.task_manager.add_task("Test Task", "Test Description")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.status, TaskStatus.PENDING)

    def test_list_tasks_empty(self):
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_list_tasks_add_tasks(self):
        self.task_manager.add_task("Task 1", "Description 1")
        self.task_manager.add_task("Task 2", "Description 2")
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_list_tasks_show_completed(self):
        task1 = self.task_manager.add_task("Task 1", "Description 1")
        task2 = self.task_manager.add_task("Task 2", "Description 2")
        self.task_manager.complete_task(task1.id)
        tasks = self.task_manager.list_tasks(show_completed=True)
        self.assertEqual(len(tasks), 2)
        tasks = self.task_manager.list_tasks(show_completed=False)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Task 2")

    def test_complete_task(self):
        task = self.task_manager.add_task("Task to complete", "")
        self.task_manager.complete_task(task.id)
        completed_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(completed_task.status, TaskStatus.COMPLETED)

    def test_delete_task(self):
        task = self.task_manager.add_task("Task to delete", "")
        task_id = task.id
        self.task_manager.delete_task(task_id)
        deleted_task = self.task_manager.get_task_by_id(task_id)
        self.assertIsNone(deleted_task)
