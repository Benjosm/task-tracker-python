# /tests/test_task_manager_add_task.py
import unittest
import datetime
from task_manager.task_manager import TaskManager

class TestTaskManagerAddTask(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager(':memory:')
        self.task_manager.storage.tasks = []
        self.task_manager.tasks = []

    def test_add_task_invalid_due_date_format(self):
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task('Invalid Date Task', 'Description', due_date='2023/12/31')
        self.assertEqual(str(context.exception), 'Due date must be in the format YYYY-MM-DD')

    def test_add_task_valid_priority(self):
        task_low = self.task_manager.add_task('Low Priority Task', 'Description', priority='low')
        self.assertEqual(task_low.priority, 'low')
        task_medium = self.task_manager.add_task('Medium Priority Task', 'Description', priority='medium')
        self.assertEqual(task_medium.priority, 'medium')
        task_high = self.task_manager.add_task('High Priority Task', 'Description', priority='high')
        self.assertEqual(task_high.priority, 'high')

    def test_add_task_invalid_priority(self):
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task('Invalid Priority Task', 'Description', priority='invalid_priority')
        self.assertEqual(str(context.exception), "Priority must be one of: low, medium, high")
