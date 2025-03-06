# tests/test_task_cli.py

import subprocess
import unittest
import os

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
        add_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'add', 'Test task'], capture_output=True, text=True, check=True)
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
        self.assertNotEqual(add_process.returncode, 0)
        self.assertIn('error:', add_process.stderr) # Expecting an error message in stderr


if __name__ == '__main__':
    unittest.main()