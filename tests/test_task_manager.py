import sys
import os
print(f"Current working directory: {os.getcwd()}")
sys.path.insert(0, '.') # Add project root to python path
from task_manager.task_manager import TaskManager

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
    try:
        task = task_manager.add_task('Test Task', 'Test Description', '2024/03/10')
    except ValueError:
        return
    assert False, "ValueError was not raised for invalid date format"

    # Clean up test file
    if os.path.exists('test_tasks.json'):
        os.remove('test_tasks.json')

def test_edit_task():
    task_manager = TaskManager('test_tasks.json') # Use a separate test json file
    task = task_manager.add_task('Original Title', 'Original Description')
    edited_task = task_manager.edit_task(task.id, 'Edited Title', 'Edited Description')
    assert edited_task is not None
    assert edited_task.title == 'Edited Title'
    assert edited_task.description == 'Edited Description'
    
    # Clean up test file
    if os.path.exists('test_tasks.json'):
        os.remove('test_tasks.json')

def test_delete_task():
    task_manager = TaskManager('test_tasks.json') # Use a separate test json file
    task = task_manager.add_task('Task to Delete', 'Description')
    task_id_to_delete = task.id
    task_manager.delete_task(task_id_to_delete)
    deleted_task = task_manager.get_task(task_id_to_delete)
    assert deleted_task is None

    # Clean up test file
    if os.path.exists('test_tasks.json'):
        os.remove('test_tasks.json')

def test_get_tasks():
    task_manager = TaskManager('test_tasks.json') # Use a separate test json file
    task1 = task_manager.add_task('Task 1', 'Description 1')
    task2 = task_manager.add_task('Task 2', 'Description 2')
    tasks = task_manager.get_tasks()
    assert len(tasks) == 2
    assert any(t.title == 'Task 1' for t in tasks)
    assert any(t.title == 'Task 2' for t in tasks)

    # Clean up test file
    if os.path.exists('test_tasks.json'):
        os.remove('test_tasks.json')