import unittest
from task_manager.task_manager import TaskManager
from task_manager.task import Task


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task = Task("Test Task", "This is a test task")
        self.task_manager.add_task(task)
        self.assertEqual(len(self.task_manager.get_all_tasks()), 1)
        self.assertEqual(self.task_manager.get_all_tasks()[0], task)

    def test_complete_task(self):
        task = Task("Test Task", "This is a test task")
        self.task_manager.add_task(task)
        self.task_manager.complete_task(task)
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = Task("Test Task", "This is a test task")
        self.task_manager.add_task(task)
        self.task_manager.delete_task(task)
        self.assertEqual(len(self.task_manager.get_all_tasks()), 0)

    def test_get_all_tasks(self):
        task1 = Task("Test Task 1", "This is test task 1")
        task2 = Task("Test Task 2", "This is test task 2")
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)


if __name__ == '__main__':
    unittest.main()