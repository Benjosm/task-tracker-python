# tests/test_task_cli.py

import subprocess
import unittest
import os
import re
import uuid

class TestTaskCLI(unittest.TestCase):

    def setUp(self):
        tasks_file = '/tmp/test_tasks.json'  # Use /tmp/test_tasks.json
        print(f"setUp: tasks_file path: {tasks_file}") # Log the path
        print(f"setUp: tasks_file exists before check: {os.path.exists(tasks_file)}")
        if os.path.exists(tasks_file):
            print(f"setUp: tasks_file exists, deleting: {tasks_file}")
            os.remove(tasks_file)
        print(f"setUp: tasks_file exists after deletion: {os.path.exists(tasks_file)}")

    def test_cli_help(self):
        process = subprocess.run(['python3', '-m', 'task_manager.task_cli', '--help'], capture_output=True, text=True, check=True)
        self.assertIn('usage: task_cli.py', process.stdout)

    def test_cli_no_command(self):
        process = subprocess.run(['python3', '-m', 'task_manager.task_cli'], capture_output=True, text=True, check=True)
        self.assertIn('usage: task_cli.py', process.stdout)

    def test_cli_list_tasks_when_tasks_exist(self):
        # Add a task
        add_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'add', 'Test task', '-d', 'Test description for list tasks test'], capture_output=True, text=True, check=True)
        self.assertIn('Task added successfully.', add_process.stdout)

        # List tasks
        list_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'list'], capture_output=True, text=True, check=True)
        print(f"List command STDOUT: \"{list_process.stdout}\"")
        print(f"List command STDERR: \"{list_process.stderr}\"")
        self.assertIn('Test task', list_process.stdout)

    def test_cli_list_tasks_when_no_tasks_exist(self):
        list_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'list'], capture_output=True, text=True, check=True)
        print(f"List command STDOUT (empty list test): \"{list_process.stdout}\"")
        print(f"List command STDERR (empty list test): \"{list_process.stderr}\"")
        self.assertIn('No tasks found.', list_process.stdout)

    def test_cli_add_task_with_description(self):
        # Add a task with description
        add_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'add', 'Test task with description', '-d', 'This is a description'], capture_output=True, text=True, check=True)
        self.assertIn('Task added successfully.', add_process.stdout)

        # List tasks and check if the description is there
        list_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'list'], capture_output=True, text=True, check=True)
        self.assertIn('Test task with description (Pending) - No due date - Priority: medium', list_process.stdout)

    def test_cli_add_task_without_description(self):
        # Try to add a task without description
        add_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'add', 'Test task without description'], capture_output=True, text=True, check=False)
        print(f"add_process.stdout: {add_process.stdout}") # ADD THIS
        print(f"add_process.stderr: {add_process.stderr}") # ADD THIS
        print(f"add_process.returncode: {add_process.returncode}") # ADD THIS
        self.assertNotEqual(add_process.returncode, 0)
        self.assertIn('Error: Description is required', add_process.stderr) # Expecting an error message in stderr

    def test_cli_complete_non_existent_task(self):
        # Try to complete a non-existent task
        complete_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'complete', '999'], capture_output=True, text=True, check=False)
        print(f"complete_process.stdout: {complete_process.stdout}") # ADD THIS
        print(f"complete_process.stderr: {complete_process.stderr}") # ADD THIS
        print(f"complete_process.returncode: {complete_process.returncode}") # ADD THIS
        self.assertNotEqual(complete_process.returncode, 0)
        self.assertIn('Error completing task 999', complete_process.stderr)

    def test_cli_delete_existing_task(self):
        # Add a task to be deleted
        add_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'add', 'Task to delete', '-d', 'Description for delete test'], capture_output=True, text=True, check=True)
        self.assertIn('Task added successfully.', add_process.stdout)

        # Extract task ID
        task_id_match = re.search(r'Task ID: ([0-9a-fA-F-]+)', add_process.stdout)
        self.assertIsNotNone(task_id_match, "Task ID not found in add task output")
        task_id = task_id_match.group(1)

        # Delete the task
        delete_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'delete', task_id], capture_output=True, text=True, check=True)
        self.assertEqual(delete_process.returncode, 0)
        self.assertIn(f'Task {task_id} deleted successfully.', delete_process.stdout)

        # List tasks and verify the task is deleted
        list_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'list'], capture_output=True, text=True, check=True)
        self.assertNotIn('Task to delete', list_process.stdout)

    def test_cli_delete_non_existent_task(self):
        # Try to delete a non-existent task
        task_id = str(uuid.uuid4())
        delete_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'delete', task_id], capture_output=True, text=True, check=False)
        self.assertNotEqual(delete_process.returncode, 0)
        self.assertIn(f'Error deleting task {task_id}: Task not found.', delete_process.stderr)

    def test_cli_view_non_existent_task(self):
        # Try to view a non-existent task
        task_id = '999' # Use a task ID that is unlikely to exist
        view_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'view', task_id], capture_output=True, text=True, check=False)
        print(f"view_process.stdout: {view_process.stdout}")
        print(f"view_process.stderr: {view_process.stderr}")
        print(f"view_process.returncode: {view_process.returncode}")
        self.assertNotEqual(view_process.returncode, 0)
        self.assertIn(f'Error viewing task {task_id}: Task not found.', view_process.stderr)


if __name__ == '__main__':
    unittest.main()