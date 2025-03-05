# tests/test_task_manager_errors.py
import unittest
import datetime
from task_manager.task_manager import TaskManager
from task_manager.task import TaskStatus

class TestTaskManagerErrors(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager(':memory:')
        self.task_manager.storage.tasks = []
        self.task_manager.tasks = []

    def test_add_task_invalid_due_date(self):
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task('Invalid Date Task', 'Description', due_date='2023-12-31-wrong')
        self.assertEqual(str(context.exception), 'Due date must be in the format YYYY-MM-DD')

    def test_edit_task_invalid_due_date(self):
        task = self.task_manager.add_task('Task to Edit', 'Description')
        with self.assertRaises(ValueError) as context:
            self.task_manager.edit_task(task.id, due_date='2024-01-15-wrong')
        self.assertEqual(str(context.exception), 'Due date must be in the format YYYY-MM-DD')

    def test_edit_task_non_existent_task(self):
        non_existent_task_id = 'non_existent_id'
        result = self.task_manager.edit_task(non_existent_task_id, title='New Title')
        self.assertFalse(result)

    def test_complete_task_non_existent_task(self):
        non_existent_task_id = 'non_existent_id'
        result = self.task_manager.complete_task(non_existent_task_id)
        self.assertFalse(result)

    def test_delete_task_non_existent_task(self):
        non_existent_task_id = 'non_existent_id'
        result = self.task_manager.delete_task(non_existent_task_id)
        self.assertFalse(result)

    def test_add_task_invalid_priority(self):
        task = self.task_manager.add_task('Invalid Priority Task', 'Description', priority='invalid_priority')
        self.assertEqual(task.priority, 'invalid_priority') # Should be handled in Task class or TaskManager

    def test_edit_task_invalid_priority(self):
        task = self.task_manager.add_task('Task to Edit Priority', 'Description')
        self.assertTrue(self.task_manager.edit_task(task.id, priority='invalid_priority'))
        edited_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(edited_task.priority, 'invalid_priority') # Should be handled in Task class or TaskManager

    def test_edit_task_invalid_priority_value_error(self):
        task = self.task_manager.add_task('Task to Edit Priority', 'Description')
        with self.assertRaises(ValueError) as context:
            self.task_manager.edit_task(task.id, priority='invalid-priority')
        self.assertEqual(str(context.exception), "Invalid priority value: invalid-priority. Priority must be one of: low, medium, high.")
