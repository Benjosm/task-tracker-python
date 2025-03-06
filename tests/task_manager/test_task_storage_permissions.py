# tests/task_manager/test_task_storage_permissions.py
import unittest
import os
from task_manager.task_storage import TaskStorage

class TestTaskStoragePermissions(unittest.TestCase):

    def setUp(self):
        self.test_dir = '/tmp/task_manager_tests'
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file = os.path.join(self.test_dir, 'test_tasks_permissions.json')
        self.task_storage = TaskStorage(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        # Optionally remove the test directory if it's empty
        if os.path.exists(self.test_dir) and not os.listdir(self.test_dir):
            os.rmdir(self.test_dir)

    def test_save_tasks_permission_error(self):
        # Create a read-only directory
        read_only_dir = os.path.join(self.test_dir, 'read_only_dir')
        os.makedirs(read_only_dir, exist_ok=True)
        os.chmod(read_only_dir, 0o555)  # Read and execute for all, no write
        read_only_file = os.path.join(read_only_dir, 'tasks.json')
        task_storage_read_only = TaskStorage(read_only_file)

        tasks = []
        with self.assertRaises(PermissionError):
            task_storage_read_only.save_tasks(tasks)

    def test_load_tasks_permission_error(self):
        # Create a non-readable file
        non_readable_file = os.path.join(self.test_dir, 'non_readable.json')
        with open(non_readable_file, 'w') as f:
            f.write('[]')
        os.chmod(non_readable_file, 0o222)  # Write only, no read
        task_storage_non_readable = TaskStorage(non_readable_file)

        with self.assertRaises(PermissionError):
            task_storage_non_readable.load_tasks()
