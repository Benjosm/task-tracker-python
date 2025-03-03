import unittest
from task_manager.task import Task


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task(title="Test Task")
        self.assertEqual(task.title, "Test Task")

if __name__ == '__main__':
    unittest.main()