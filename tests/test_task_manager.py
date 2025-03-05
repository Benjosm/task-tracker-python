# /tests/test_task_manager.py
import unittest
from task_manager.task_manager import TaskManager
from task_manager.task import Task
from task_manager.task import TaskStatus

class TestTaskManager(unittest.TestCase):

    def setUp(self): # setup method is called before each test method
        self.task_manager = TaskManager(':memory:') # Use an in-memory storage for tests
        self.task_manager.storage.tasks = [] # clear existing tasks
        self.task_manager.tasks = [] # clear existing tasks

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

if __name__ == '__main__':
    unittest.main()