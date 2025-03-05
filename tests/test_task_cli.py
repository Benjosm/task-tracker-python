# tests/test_task_cli.py

import subprocess
import unittest

class TestTaskCLI(unittest.TestCase):

    def test_cli_help(self):
        process = subprocess.run(['python3', '/usr/src/task-tracker-python/task_manager/task_cli.py', '--help'], capture_output=True, text=True, check=True)
        self.assertIn('usage: task_cli.py', process.stdout)

    def test_cli_no_command(self):
        process = subprocess.run(['python3', '/usr/src/task-tracker-python/task_manager/task_cli.py'], capture_output=True, text=True, check=True)
        self.assertIn('usage: task_cli.py', process.stdout)

if __name__ == '__main__':
    unittest.main()