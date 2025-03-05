# /tests/test_task_manager.py
import unittest
import os

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

if __name__ == '__main__':
    unittest.main()