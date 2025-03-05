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

    def test_minimal(self):
        self.assertTrue(True)