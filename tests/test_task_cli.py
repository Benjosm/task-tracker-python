# tests/test_task_cli.py

import subprocess
import unittest
import os

class TestTaskCLI(unittest.TestCase):

    def setUp(self):
        tasks_file = '/tmp/task_manager_tests/test_tasks.json'
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
        self.assertIn('Task added with ID', add_process.stdout)

        # List tasks
        list_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'list'], capture_output=True, text=True, check=True)
        print("List command STDOUT: \"" + list_process.stdout + "\"")
        print("List command STDERR: \"" + list_process.stderr + "\"")
        self.assertIn('Test task', list_process.stdout)

    def test_cli_list_tasks_when_no_tasks_exist(self):
        list_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'list'], capture_output=True, text=True, check=True)
        print("List command STDOUT (empty list test): \"" + list_process.stdout + "\"")
        print("List command STDERR (empty list test): \"" + list_process.stderr + "\"")
        self.assertIn('No tasks found.', list_process.stdout)


if __name__ == '__main__':
    unittest.main()