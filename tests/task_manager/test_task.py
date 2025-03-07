# tests/task_manager/test_task.py

import unittest
from task_manager.task import Task, TaskStatus
import datetime
import uuid
import inspect

class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task("Test Task", "This is a test task", due_date=datetime.date(2024, 1, 15), priority="high")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertEqual(task.due_date, datetime.date(2024, 1, 15))
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.status, TaskStatus.PENDING)
        self.assertIsNotNone(task.id)
        self.assertIsInstance(task.id, str)
        self.assertIsInstance(uuid.UUID(task.id), uuid.UUID) # Valid UUID
        self.assertEqual(task.created_date, datetime.date.today())
        self.assertIsNone(task.completed_date)

    def test_task_creation_minimal(self):
        task = Task("Minimal Task")
        self.assertEqual(task.title, "Minimal Task")
        self.assertEqual(task.description, "")
        self.assertIsNone(task.due_date)
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.status, TaskStatus.PENDING)
        self.assertIsNotNone(task.id)
        self.assertEqual(task.created_date, datetime.date.today())
        self.assertIsNone(task.completed_date)

    def test_task_to_dict(self):
        task = Task("Dict Task", "For dict test", due_date=datetime.date(2024, 2, 20), priority="low")
        task_dict = task.to_dict()
        self.assertEqual(task_dict['title'], "Dict Task")
        self.assertEqual(task_dict['description'], "For dict test")
        self.assertEqual(task_dict['due_date'], "2024-02-20")
        self.assertEqual(task_dict['priority'], "low")
        self.assertEqual(task_dict['status'], "Pending")
        self.assertEqual(task_dict['created_date'], datetime.date.today().isoformat())
        self.assertIsInstance(task_dict['id'], str)

    def test_task_from_dict(self):
        task_dict = {
            'id': str(uuid.uuid4()),
            'title': 'From Dict Task',
            'description': 'Creating task from dict',
            'due_date': '2024-03-10',
            'priority': 'high',
            'status': 'In Progress',
            'created_date': datetime.date(2024, 1, 1).isoformat(),
            'completed_date': None
        }
        task = Task.from_dict(task_dict)
        self.assertEqual(task.title, "From Dict Task")
        self.assertEqual(task.description, "Creating task from dict")
        self.assertEqual(task.due_date, datetime.date(2024, 3, 10))
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)
        self.assertEqual(task.id, task_dict['id'])
        self.assertEqual(task.created_date, datetime.date(2024, 1, 1))
        self.assertIsNone(task.completed_date)

    def test_task_str_representation(self):
        task = Task("String Task", priority="high", due_date=datetime.date(2024, 4, 1))
        expected_str = f"String Task (Pending) - Due: 2024-04-01 - Priority: high"
        self.assertEqual(str(task), expected_str)

    def test_task_status_enum(self):
        task = Task("Status Task")
        self.assertEqual(task.status, TaskStatus.PENDING)
        task.status = TaskStatus.IN_PROGRESS # How to change status? no method to change status
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)
        task.status = TaskStatus.COMPLETED
        self.assertEqual(task.status, TaskStatus.COMPLETED)

    def test_task_creation_empty_title(self):
        task = Task("")
        self.assertEqual(task.title, "")

    def test_task_creation_long_description(self):
        long_description = "This is a very long description" * 100
        task = Task("Long Description Task", description=long_description)
        self.assertEqual(task.description, long_description)

    def test_task_creation_past_due_date(self):
        past_due_date = datetime.date(2023, 1, 1)
        task = Task("Past Due Date Task", due_date=past_due_date)
        self.assertEqual(task.due_date, past_due_date)

    def test_task_creation_invalid_priority(self):
        task = Task("Invalid Priority Task", priority="invalid")
        self.assertEqual(task.priority, "invalid") # It should accept invalid priority, no validation

    def test_task_from_dict_missing_title(self):
        task_dict = {
            'id': str(uuid.uuid4()),
            'description': 'Creating task from dict',
            'due_date': '2024-03-10',
            'priority': 'high',
            'status': 'In Progress',
            'created_date': datetime.date(2024, 1, 1).isoformat(),
            'completed_date': None
        }
        with self.assertRaises(ValueError) as context:
            Task.from_dict(task_dict)
        self.assertIn("title", str(context.exception).lower())

    def test_task_from_dict_missing_id(self):
        task_dict = {
            'title': 'Missing ID Task',
            'description': 'Creating task from dict without id',
            'due_date': '2024-03-15',
            'priority': 'medium',
            'status': 'Pending',
            'created_date': datetime.date(2024, 1, 5).isoformat(),
            'completed_date': None
        }
        with self.assertRaises(ValueError) as context:
            Task.from_dict(task_dict)
        self.assertIn("id", str(context.exception).lower())

class TestTaskDocumentation(unittest.TestCase):

    def test_task_class_docstring(self):
        self.assertIsNotNone(Task.__doc__, "Task class should have a docstring")
        self.assertGreater(len(Task.__doc__), 0, "Task class docstring should not be empty")

    def test_task_init_docstring(self):
        self.assertIsNotNone(Task.__init__.__doc__, "Task.__init__ should have a docstring")
        self.assertGreater(len(Task.__init__.__doc__), 0, "Task.__init__ docstring should not be empty")
        
    def test_task_to_dict_docstring(self):
        self.assertIsNotNone(Task.to_dict.__doc__, "Task.to_dict should have a docstring")
        self.assertGreater(len(Task.to_dict.__doc__), 0, "Task.to_dict docstring should not be empty")

    def test_task_from_dict_docstring(self):
        self.assertIsNotNone(Task.from_dict.__doc__, "Task.from_dict should have a docstring")
        self.assertGreater(len(Task.from_dict.__doc__), 0, "Task.from_dict docstring should not be empty")

    def test_task_str_docstring(self):
        self.assertIsNotNone(Task.__str__.__doc__, "Task.__str__ should have a docstring")
        self.assertGreater(len(Task.__str__.__doc__), 0, "Task.__str__ docstring should not be empty")

    def test_task_init_type_hints(self):
        signature = inspect.signature(Task.__init__)
        self.assertTrue(signature.parameters['title'].annotation != inspect.Parameter.empty, "Task.__init__ should have type hint for title")
        self.assertTrue(signature.parameters['description'].annotation != inspect.Parameter.empty, "Task.__init__ should have type hint for description")
        self.assertTrue(signature.parameters['due_date'].annotation != inspect.Parameter.empty, "Task.__init__ should have type hint for due_date")
        self.assertTrue(signature.parameters['priority'].annotation != inspect.Parameter.empty, "Task.__init__ should have type hint for priority")
        self.assertTrue(signature.parameters['status'].annotation != inspect.Parameter.empty, "Task.__init__ should have type hint for status")

    def test_task_to_dict_type_hints(self):
        signature = inspect.signature(Task.to_dict)
        self.assertTrue(signature.return_annotation != inspect.Signature.empty, "Task.to_dict should have return type hint")

    def test_task_from_dict_type_hints(self):
        signature = inspect.signature(Task.from_dict)
        self.assertTrue(signature.parameters['data'].annotation != inspect.Parameter.empty, "Task.from_dict should have type hint for data")
        self.assertTrue(signature.return_annotation != inspect.Signature.empty, "Task.from_dict should have return type hint")

    def test_task_str_type_hints(self):
        signature = inspect.signature(Task.__str__)
        self.assertTrue(signature.return_annotation != inspect.Signature.empty, "Task.__str__ should have return type hint")

if __name__ == '__main__':
    unittest.main()