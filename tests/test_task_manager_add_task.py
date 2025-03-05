# /tests/test_task_manager_add_task.py
import unittest
import datetime

from task_manager.task_manager import TaskManager
from task_manager.task import Task

class TestTaskManagerAddTask(unittest.TestCase):

    def setUp(self): # setup method is called before each test method
        self.task_manager = TaskManager(':memory:') # Use an in-memory storage for tests
        self.task_manager.storage.tasks = [] # clear existing tasks
        self.task_manager.tasks = [] # clear existing tasks
        self.base_dir = '/usr/src/task-tracker-python'

    def test_add_task_invalid_due_date_format(self):
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task('Invalid Date Task', 'Description', due_date='2023/12/31')
        self.assertEqual(str(context.exception), 'Due date must be in the format YYYY-MM-DD')

    def test_add_task_default_priority(self):
        task = self.task_manager.add_task('Default Priority Task', 'Description')
        self.assertEqual(task.priority, 'medium')

    def test_add_task_invalid_priority(self):
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task('Invalid Priority Task', 'Description', priority='invalid_priority')
        self.assertEqual(str(context.exception), 'Priority must be one of: low, medium, high')
