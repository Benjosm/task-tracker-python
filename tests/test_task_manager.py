# /tests/test_task_manager.py
import unittest
import os
import datetime

from task_manager.task_manager import TaskManager
from task_manager.task import Task
from task_manager.task import TaskStatus

class TestTaskManager(unittest.TestCase):

    def setUp(self): # setup method is called before each test method
        self.task_manager = TaskManager(':memory:') # Use an in-memory storage for tests
        self.task_manager.storage.tasks = [] # clear existing tasks
        self.task_manager.tasks = [] # clear existing tasks
        self.base_dir = '/usr/src/task-tracker-python'

    def test_add_task(self):
        task = self.task_manager.add_task('Test Task', 'Test Description')
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Description')
        self.assertEqual(task.status, TaskStatus.PENDING)

    def test_list_tasks_empty(self):
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_list_tasks_not_empty(self):
        self.task_manager.add_task('Task 1', 'Description 1')
        self.task_manager.add_task('Task 2', 'Description 2')
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, 'Task 1')
        self.assertEqual(tasks[1].title, 'Task 2')

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
        self.assertEqual(tasks[0].title, 'Task 2')

    def test_project_structure(self):
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'task_manager')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'tests')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'task_manager', '__init__.py')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'task_manager', 'task_manager.py')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'task_manager', 'task_storage.py')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'task_manager', 'task.py')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'tests', 'test_task_manager.py')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'main.py')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'README.md')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'setup.py')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, '.gitignore')))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'LICENSE')))

    def test_get_statistics(self):
        self.task_manager.add_task('Task 1', 'Description 1', priority='high')
        self.task_manager.add_task('Task 2', 'Description 2', priority='medium')
        self.task_manager.add_task('Task 3', 'Description 3', priority='low')
        task4 = self.task_manager.add_task('Task 4', 'Description 4', priority='low')
        self.task_manager.complete_task(task4.id)

        stats = self.task_manager.get_statistics()
        self.assertEqual(stats['total'], 4)
        self.assertEqual(stats['completed'], 1)
        self.assertEqual(stats['pending'], 3)
        self.assertEqual(stats['priorities']['high'], 1)
        self.assertEqual(stats['priorities']['medium'], 1)
        self.assertEqual(stats['priorities']['low'], 2)

    def test_delete_task(self):
        task1 = self.task_manager.add_task('Task 1', 'Description 1')
        task2 = self.task_manager.add_task('Task 2', 'Description 2')
        self.assertTrue(self.task_manager.delete_task(task1.id))
        self.assertFalse(self.task_manager.get_task_by_id(task1.id))
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, 'Task 2')
        self.assertFalse(self.task_manager.delete_task('non_existent_id'))

    def test_get_task_by_id(self):
        task1 = self.task_manager.add_task('Task 1', 'Description 1')
        task2 = self.task_manager.add_task('Task 2', 'Description 2')
        retrieved_task1 = self.task_manager.get_task_by_id(task1.id)
        retrieved_task2 = self.task_manager.get_task_by_id(task2.id)
        self.assertEqual(retrieved_task1.title, 'Task 1')
        self.assertEqual(retrieved_task2.title, 'Task 2')
        self.assertIsNone(self.task_manager.get_task_by_id('non_existent_id'))

    def test_add_task_with_due_date(self):
        due_date_str = '2023-12-31'
        due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
        task = self.task_manager.add_task('Task with Due Date', 'Description', due_date=due_date_str)
        self.assertIsInstance(task, Task)
        self.assertEqual(task.due_date, due_date)

    def test_edit_task_title(self):
        task = self.task_manager.add_task('Original Title', 'Description')
        self.assertTrue(self.task_manager.edit_task(task.id, title='New Title'))
        edited_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(edited_task.title, 'New Title')

    def test_edit_task_description(self):
        task = self.task_manager.add_task('Title', 'Original Description')
        self.assertTrue(self.task_manager.edit_task(task.id, description='New Description'))
        edited_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(edited_task.description, 'New Description')

    def test_edit_task_due_date(self):
        task = self.task_manager.add_task('Title', 'Description')
        due_date_str = '2024-01-15'
        due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
        self.assertTrue(self.task_manager.edit_task(task.id, due_date=due_date_str))
        edited_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(edited_task.due_date, due_date)

    def test_edit_task_priority(self):
        task = self.task_manager.add_task('Title', 'Description')
        self.assertTrue(self.task_manager.edit_task(task.id, priority='high'))
        edited_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(edited_task.priority, 'high')

    def test_edit_task_invalid_priority(self):
        task = self.task_manager.add_task('Title', 'Description')
        with self.assertRaises(ValueError) as context:
            self.task_manager.edit_task(task.id, priority='invalid_priority')
        self.assertEqual(str(context.exception), 'Priority must be one of: low, medium, high')

    def test_complete_task(self):
        task = self.task_manager.add_task('Complete Task Test', 'Description for complete task test')
        self.assertEqual(task.status, TaskStatus.PENDING)
        completion_result = self.task_manager.complete_task(task.id)
        self.assertTrue(completion_result)
        completed_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(completed_task.status, TaskStatus.COMPLETED)
        self.assertIsNotNone(completed_task.completed_date)

if __name__ == '__main__':
    unittest.main()