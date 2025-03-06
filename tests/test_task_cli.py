# tests/test_task_cli.py

import subprocess
import unittest

class TestTaskCLI(unittest.TestCase):

    def test_cli_help(self):
        process = subprocess.run(['python3', '-m', 'task_manager.task_cli', '--help'], capture_output=True, text=True, check=True)
        self.assertIn('usage: task_cli.py', process.stdout)

    def test_cli_no_command(self):
        process = subprocess.run(['python3', '-m', 'task_manager.task_cli'], capture_output=True, text=True, check=True)
        self.assertIn('usage: task_cli.py', process.stdout)

    def test_cli_list_tasks_when_tasks_exist(self):
        # Add a task
        add_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'add', 'Test task'], capture_output=True, text=True, check=True)
        self.assertIn('Task added successfully', add_process.stdout)

        # List tasks
        list_process = subprocess.run(['python3', '-m', 'task_manager.task_cli', 'list'], capture_output=True, text=True, check=True)
        self.assertIn('Test task', list_process.stdout)


if __name__ == '__main__':
    unittest.main()