import sys
sys.path.insert(0, '.') # Add project root to python path
from task_manager.task_manager import TaskManager
import os

def test_add_task():
    task_manager = TaskManager('test_tasks.json') # Use a separate test json file
    task = task_manager.add_task('Test Task', 'Test Description')
    assert task is not None
    assert task.title == 'Test Task'
    assert task.description == 'Test Description'
    
    # Clean up test file
    if os.path.exists('test_tasks.json'):
        os.remove('test_tasks.json')

def test_add_task_no_description():
    task_manager = TaskManager('test_tasks.json') # Use a separate test json file
    task = task_manager.add_task('Test Task')
    assert task is not None
    assert task.title == 'Test Task'
    assert task.description == ''
    
    # Clean up test file
    if os.path.exists('test_tasks.json'):
        os.remove('test_tasks.json')

def test_add_task_with_status():
    task_manager = TaskManager('test_tasks.json') # Use a separate test json file
    task = task_manager.add_task('Test Task', 'Test Description', 'Pending')
    assert task is not None
    assert task.title == 'Test Task'
    assert task.description == 'Test Description'
    assert task.status == 'Pending'

    # Clean up test file
    if os.path.exists('test_tasks.json'):
        os.remove('test_tasks.json')
