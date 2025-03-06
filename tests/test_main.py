# tests/test_main.py

import subprocess

def test_main_entry_point_help():
    process = subprocess.run(['python3', 'main.py', '--help'], capture_output=True, text=True, check=False)
    assert process.returncode == 0
    expected_help_message = '''usage: main.py [-h] [--tasks-file TASKS_FILE] {add,list,complete,delete} ...\n\nTask CLI\n\npositional arguments:\n  {add,list,complete,delete}
    add                 Add a new task
    list                List tasks
    complete            Complete a task
    delete              Delete a task\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --tasks-file TASKS_FILE
                        Path to the tasks JSON file\n'''
    assert expected_help_message in process.stdout