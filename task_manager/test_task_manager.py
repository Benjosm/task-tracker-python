# task_manager/test_task_manager.py

import unittest
from task_manager.task_manager import TaskManager
from task_manager.task import TaskStatus
import datetime

class TestTaskManager(unittest.TestCase):

    def setUp(self): # setup method to create TaskManager instance before each test
        self.task_manager = TaskManager()
        self.task_manager.clear_tasks()

    def test_add_task(self): 
        task = self.task_manager.add_task("Test Task", "Test Description")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.status, TaskStatus.PENDING)

    def test_list_tasks_empty(self): 
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_list_tasks_add_tasks(self): 
        self.task_manager.add_task("Task 1", "Description 1")
        self.task_manager.add_task("Task 2", "Description 2")
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_list_tasks_show_completed(self): 
        task1 = self.task_manager.add_task("Task 1", "Description 1")
        task2 = self.task_manager.add_task("Task 2", "Description 2")
        self.task_manager.complete_task(task1.id)
        tasks = self.task_manager.list_tasks(show_completed=True)
        self.assertEqual(len(tasks), 2)
        tasks = self.task_manager.list_tasks(show_completed=False)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Task 2")

    def test_complete_task(self): 
        task = self.task_manager.add_task("Task to complete", "")
        self.task_manager.complete_task(task.id)
        completed_task = self.task_manager.get_task_by_id(task.id)
        self.assertEqual(completed_task.status, TaskStatus.COMPLETED)

    def test_delete_task(self): 
        task = self.task_manager.add_task("Task to delete", "")
        task_id = task.id
        self.task_manager.delete_task(task_id)
        deleted_task = self.task_manager.get_task_by_id(task_id)
        self.assertIsNone(deleted_task)

    def test_edit_task(self):
        task = self.task_manager.add_task("Original Title", "Original Description", due_date="2024-01-01", priority="low")
        task_id = task.id

        # Edit title and description
        self.task_manager.edit_task(task_id, title="Edited Title", description="Edited Description")
        edited_task = self.task_manager.get_task_by_id(task_id)
        self.assertEqual(edited_task.title, "Edited Title")
        self.assertEqual(edited_task.description, "Edited Description")
        self.assertEqual(edited_task.due_date, datetime.date(2024, 1, 1))
        self.assertEqual(edited_task.priority, "low")

        # Edit due_date and priority
        self.task_manager.edit_task(task_id, due_date="2024-02-15", priority="high")
        edited_task = self.task_manager.get_task_by_id(task_id)
        self.assertEqual(edited_task.title, "Edited Title")
        self.assertEqual(edited_task.description, "Edited Description")
        self.assertEqual(edited_task.due_date, datetime.date(2024, 2, 15))
        self.assertEqual(edited_task.priority, "high")

        # Edit all fields
        self.task_manager.edit_task(task_id, title="New Title", description="New Description", due_date="2024-03-20", priority="medium")
        edited_task = self.task_manager.get_task_by_id(task_id)
        self.assertEqual(edited_task.title, "New Title")
        self.assertEqual(edited_task.description, "New Description")
        self.assertEqual(edited_task.due_date, datetime.date(2024, 3, 20))
        self.assertEqual(edited_task.priority, "medium")

    def test_edit_task_not_found(self):
        task_id = "non_existent_id"
        result = self.task_manager.edit_task(task_id, title="Should not edit")
        self.assertFalse(result)

    def test_add_task_invalid_priority(self):
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task("Invalid Priority Task", priority="invalid")
        self.assertEqual(str(context.exception), "Priority must be one of 'low', 'medium', 'high'")