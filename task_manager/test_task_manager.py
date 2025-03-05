import unittest
from task_manager.task_manager import TaskManager
from task_manager.task import TaskStatus

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
        task1 = self.task_manager.add_task('Task 1', 'Description 1')
        task2 = self.task_manager.add_task('Task 2', 'Description 2')
        retrieved_task = self.task_manager.get_task_by_id(task2.id)
        self.assertEqual(retrieved_task.id, task2.id)
        self.assertEqual(retrieved_task.title, 'Task 2')

    def test_get_task_by_id_not_found(self):
        retrieved_task = self.task_manager.get_task_by_id('nonexistent_id')
        self.assertIsNone(retrieved_task)

    def test_get_statistics(self):
        self.task_manager.add_task('Task 1', 'Description 1', priority='high')
        self.task_manager.add_task('Task 2', 'Description 2', priority='medium')
        task3 = self.task_manager.add_task('Task 3', 'Description 3', priority='low')
        self.task_manager.complete_task(task3.id)
        stats = self.task_manager.get_statistics()
        self.assertEqual(stats['total'], 3)
        self.assertEqual(stats['completed'], 1)
        self.assertEqual(stats['pending'], 2)
        self.assertEqual(stats['priorities']['high'], 1)
        self.assertEqual(stats['priorities']['medium'], 1)
        self.assertEqual(stats['priorities']['low'], 1)

    def test_edit_task(self):
        task = self.task_manager.add_task('Original Title', 'Original Description')
        updated_task = self.task_manager.edit_task(task.id, 'Updated Title', 'Updated Description')
        self.assertEqual(updated_task.title, 'Updated Title')
        self.assertEqual(updated_task.description, 'Updated Description')

    def test_edit_task_description(self):
        task = self.task_manager.add_task('Original Title', 'Original Description')
        updated_task = self.task_manager.edit_task(task.id, None, 'Updated Description')
        self.assertEqual(updated_task.title, 'Original Title')
        self.assertEqual(updated_task.description, 'Updated Description')

    def test_edit_task_title(self):
        task = self.task_manager.add_task('Original Title', 'Original Description')
        updated_task = self.task_manager.edit_task(task.id, 'Updated Title', None)
        self.assertEqual(updated_task.title, 'Updated Title')
        self.assertEqual(updated_task.description, 'Original Description')


if __name__ == '__main__':
    unittest.main()