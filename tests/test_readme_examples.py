# tests/test_readme_examples.py
import subprocess

def test_readme_examples():
    commands = [
        'python3 -m task_manager.task_cli add "Implement new feature" -d "Add user authentication" --due 2025-04-01 -p high',
        'python3 -m task_manager.task_cli list',
        'python3 -m task_manager.task_cli list -a',
        'python3 -m task_manager.task_cli list -v',
        'python3 -m task_manager.task_cli complete 1',
        'python3 -m task_manager.task_cli delete 1',
        'python3 -m task_manager.task_cli view 1',
        'python3 -m task_manager.task_cli stats',
        'python3 -m task_manager.task_cli --help'
    ]
    for command in commands:
        process = subprocess.run(command, shell=True, capture_output=True)
        assert process.returncode == 0
