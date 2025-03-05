# /tests/test_task_manager_errors.py
import unittest
from task_manager.task_manager import TaskManager

class TestTaskManagerErrors(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager(':memory:')
        self.task_manager.storage.tasks = []
        self.task_manager.tasks = []

    def test_add_task_empty_title(self):
        with self.assertRaises(ValueError):
            self.task_manager.add_task('', 'Description')

    def test_add_task_title_too_long(self):
        long_title = 'A' * 101  # Assuming title limit is 100
        with self.assertRaises(ValueError):
            self.task_manager.add_task(long_title, 'Description')

    def test_edit_task_invalid_id(self):
        with self.assertRaises(ValueError):
            self.task_manager.edit_task('invalid_id', title='New Title')

    def test_edit_task_empty_title(self):
        task = self.task_manager.add_task('Original Title', 'Description')
        with self.assertRaises(ValueError):
            self.task_manager.edit_task(task.id, title='')

if __name__ == '__main__':
    unittest.main()