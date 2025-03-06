# tests/test_docstrings.py

import unittest
import inspect
from task_manager.task import Task, TaskStatus
from task_manager.task_manager import TaskManager
from task_manager.task_storage import TaskStorage
from task_manager.task_cli import main

class TestDocstrings(unittest.TestCase):

    def test_task_module_docstring(self):
        self.assertIsNotNone(Task.__doc__, "Task module should have a docstring")

    def test_taskstatus_enum_docstring(self):
        self.assertIsNotNone(TaskStatus.__doc__, "TaskStatus enum should have a docstring")

    def test_task_class_docstring(self):
        self.assertIsNotNone(Task.__doc__, "Task class should have a docstring")

    def test_task_init_docstring(self):
        self.assertIsNotNone(Task.__init__.__doc__, "Task.__init__ should have a docstring")

    def test_task_to_dict_docstring(self):
        self.assertIsNotNone(Task.to_dict.__doc__, "Task.to_dict should have a docstring")

    def test_task_from_dict_docstring(self):
        self.assertIsNotNone(Task.from_dict.__doc__, "Task.from_dict should have a docstring")

    def test_task_str_docstring(self):
        self.assertIsNotNone(Task.__str__.__doc__, "Task.__str__ should have a docstring")

    def test_taskmanager_module_docstring(self):
        self.assertIsNotNone(TaskManager.__doc__, "TaskManager module should have a docstring")

    def test_taskmanager_class_docstring(self):
        self.assertIsNotNone(TaskManager.__doc__, "TaskManager class should have a docstring")

    def test_taskmanager_init_docstring(self):
        self.assertIsNotNone(TaskManager.__init__.__doc__, "TaskManager.__init__ should have a docstring")

    def test_taskmanager_clear_tasks_docstring(self):
        self.assertIsNotNone(TaskManager.clear_tasks.__doc__, "TaskManager.clear_tasks should have a docstring")

    def test_taskmanager_add_task_docstring(self):
        self.assertIsNotNone(TaskManager.add_task.__doc__, "TaskManager.add_task should have a docstring")

    def test_taskmanager_list_tasks_docstring(self):
        self.assertIsNotNone(TaskManager.list_tasks.__doc__, "TaskManager.list_tasks should have a docstring")

    def test_taskmanager_complete_task_docstring(self):
        self.assertIsNotNone(TaskManager.complete_task.__doc__, "TaskManager.complete_task should have a docstring")

    def test_taskmanager_delete_task_docstring(self):
        self.assertIsNotNone(TaskManager.delete_task.__doc__, "TaskManager.delete_task should have a docstring")

    def test_taskmanager_get_task_by_id_docstring(self):
        self.assertIsNotNone(TaskManager.get_task_by_id.__doc__, "TaskManager.get_task_by_id should have a docstring")

    def test_taskmanager_get_statistics_docstring(self):
        self.assertIsNotNone(TaskManager.get_statistics.__doc__, "TaskManager.get_statistics should have a docstring")

    def test_taskmanager_edit_task_docstring(self):
        self.assertIsNotNone(TaskManager.edit_task.__doc__, "TaskManager.edit_task should have a docstring")

    def test_taskstorage_module_docstring(self):
        self.assertIsNotNone(TaskStorage.__doc__, "TaskStorage module should have a docstring")

    def test_taskstorage_class_docstring(self):
        self.assertIsNotNone(TaskStorage.__doc__, "TaskStorage class should have a docstring")

    def test_taskstorage_init_docstring(self):
        self.assertIsNotNone(TaskStorage.__init__.__doc__, "TaskStorage.__init__ should have a docstring")

    def test_taskstorage_save_tasks_docstring(self):
        self.assertIsNotNone(TaskStorage.save_tasks.__doc__, "TaskStorage.save_tasks should have a docstring")

    def test_taskstorage_load_tasks_docstring(self):
        self.assertIsNotNone(TaskStorage.load_tasks.__doc__, "TaskStorage.load_tasks should have a docstring")

    def test_task_cli_module_docstring(self):
        self.assertIsNotNone(main.__doc__, "task_cli module should have a docstring")

    def test_task_cli_main_function_docstring(self):
        self.assertIsNotNone(main.__doc__, "task_cli.main function should have a docstring")
