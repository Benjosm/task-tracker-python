import unittest
from task_manager.task_manager import TaskManager
from task_manager.task import TaskStatus
import datetime


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager(':memory:') # Use in-memory storage for tests
        self.task_manager.tasks = [] # Clear tasks before each test

    def test_add_task(self):
        task = self.task_manager.add_task('Test task', 'This is a test description')
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, 'Test task')
        self.assertEqual(task.description, 'This is a test description')
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_list_tasks(self):
        self.task_manager.add_task('Task 1', 'Description 1')
        self.task_manager.add_task('Task 2', 'Description 2')
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 2)

    def test_list_tasks_show_completed(self):
        task1 = self.task_manager.add_task('Task 1', 'Description 1')
        task2 = self.task_manager.add_task('Task 2', 'Description 2')
        self.task_manager.complete_task(task1.id)
        tasks = self.task_manager.list_tasks(show_completed=True)
        self.assertEqual(len(tasks), 2)

    def test_list_tasks_hide_completed(self):
        task1 = self.task_manager.add_task('Task 1', 'Description 1')
        task2 = self.task_manager.add_task('Task 2', 'Description 2')
        self.task_manager.complete_task(task1.id)
        tasks = self.task_manager.list_tasks(show_completed=False)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, task2.id)

    def test_complete_task(self):
        task = self.task_manager.add_task('Task to complete', 'Description')
        completed = self.task_manager.complete_task(task.id)
        self.assertTrue(completed)
        task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(task.status, TaskStatus.COMPLETED)

    def test_complete_task_not_found(self):
        completed = self.task_manager.complete_task('nonexistent_id')
        self.assertFalse(completed)

    def test_delete_task(self):
        task = self.task_manager.add_task('Task to delete', 'Description')
        deleted = self.task_manager.delete_task(task.id)
        self.assertTrue(deleted)
        task = self.task_manager.get_task_by_id(task.id)
        self.assertIsNone(task)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_delete_task_not_found(self):
        deleted = self.task_manager.delete_task('nonexistent_id')
        self.assertFalse(deleted)

    def test_get_task_by_id(self):
        task1 = self.task_manager.add_task('Task 1', 'Description 1', priority='high')
        task2 = self.task_manager.add_task('Task 2', 'Description 2', priority='medium')
        task3 = self.task_manager.add_task('Task 3', 'Description 3', priority='low')
        self.task_manager.complete_task(task3.id)
        stats = self.task_manager.get_statistics()

    def test_edit_task_invalid_due_date_format(self):
        task = self.task_manager.add_task('Task to edit', 'Description', due_date='2023-12-31')
        with self.assertRaises(ValueError):
            self.task_manager.edit_task(task.id, due_date='invalid-date-format')

    def test_edit_task(self):
        task = self.task_manager.add_task('Task to edit', 'Description')
        edited_task = self.task_manager.edit_task(task.id, title='Edited title', description='Edited description')
        self.assertTrue(edited_task)
        task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(task.title, 'Edited title')
        self.assertEqual(task.description, 'Edited description')

    def test_get_statistics(self):
        task1 = self.task_manager.add_task('Task 1', 'Description 1', priority='high')
        task2 = self.task_manager.add_task('Task 2', 'Description 2', priority='medium')
        task3 = self.task_manager.add_task('Task 3', 'Description 3', priority='low')
        self.task_manager.complete_task(task2.id)
        stats = self.task_manager.get_statistics()
        self.assertEqual(stats['total_tasks'], 3)
        self.assertEqual(stats['completed_tasks'], 1)
        self.assertEqual(stats['pending_tasks'], 2)
        self.assertEqual(stats['high_priority_tasks'], 1)
        self.assertEqual(stats['medium_priority_tasks'], 1)
        self.assertEqual(stats['low_priority_tasks'], 1)

    def test_edit_task_priority(self):
        task = self.task_manager.add_task('Task to edit priority', 'Description', priority='low')
        edited_task = self.task_manager.edit_task(task.id, priority='high')
        self.assertTrue(edited_task)
        task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(task.priority, 'high')

    def test_edit_task_due_date(self):
        task = self.task_manager.add_task('Task to edit', 'Description')
        due_date = datetime.date(2024, 1, 1)
        edited_task = self.task_manager.edit_task(task.id, due_date=due_date)
        self.assertTrue(edited_task)
        task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(task.due_date, due_date)
