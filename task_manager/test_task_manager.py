import unittest
from task_manager.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def test_add_task(self):
        task_manager = TaskManager()
        task_manager.add_task("Test Task", "Test Description")
        tasks = task_manager.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], "Test Task")
        self.assertEqual(tasks[0]['description'], "Test Description")

    def test_get_tasks(self):
        task_manager = TaskManager()
        task_manager.add_task("Task 1", "Description 1")
        task_manager.add_task("Task 2", "Description 2")
        tasks = task_manager.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['title'], "Task 1")
        self.assertEqual(tasks[1]['title'], "Task 2")

    def test_minimal(self):
        self.assertTrue(True)