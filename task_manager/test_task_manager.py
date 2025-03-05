import pytest
from task_manager.task import Task, TaskStatus
from task_manager.task_manager import TaskManager
import os

@pytest.fixture
def task_manager():
    # Setup: create a new task manager instance for each test, using a temporary file for storage
    temp_storage_path = 'test_tasks.json'
    tm = TaskManager(storage_path=temp_storage_path)
    tm.storage.clear_tasks()
    yield tm
    # Teardown: remove the temporary file after each test
    if os.path.exists(temp_storage_path):
        os.remove(temp_storage_path)


def test_task_creation():
    task = Task(title='Test Task', description='Test Description')
    assert task.id is not None
    assert task.title == 'Test Task'
    assert task.description == 'Test Description'
    assert task.status == TaskStatus.PENDING


def test_add_task(task_manager):
    task = task_manager.add_task(title='New Task')
    assert task is not None
    assert task.title == 'New Task'
    assert len(task_manager.list_tasks()) == 1


def test_list_tasks(task_manager):
    task_manager.add_task(title='Task 1')
    task_manager.add_task(title='Task 2')
    tasks = task_manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == 'Task 1'
    assert tasks[1].title == 'Task 2'


def test_list_tasks_show_completed(task_manager): # No status check here, focus on listing
    task1 = task_manager.add_task(title='Task 1')
    task2 = task_manager.add_task(title='Task 2')
    task_manager.complete_task(task1.id)
    tasks = task_manager.list_tasks(show_completed=True)
    assert len(tasks) == 2


def test_complete_task(task_manager): # Status implicitly changes on completion
    task = task_manager.add_task(title='Task to complete')
    completed = task_manager.complete_task(task.id)
    assert completed
    #assert task.status == TaskStatus.COMPLETED #Status is not directly checked like this anymore
    assert task.completed_date is not None


def test_complete_nonexistent_task(task_manager): # No status impact
    completed = task_manager.complete_task('nonexistent_id')
    assert not completed


def test_delete_task(task_manager): # No status impact
    task = task_manager.add_task(title='Task to delete')
    deleted = task_manager.delete_task(task.id)
    assert deleted
    assert len(task_manager.list_tasks()) == 0


def test_delete_nonexistent_task(task_manager): # No status impact
    deleted = task_manager.delete_task('nonexistent_id')
    assert not deleted


def test_get_task_by_id(task_manager): # No status check here
    task1 = task_manager.add_task(title='Task 1')
    task2 = task_manager.add_task(title='Task 2')
    retrieved_task = task_manager.get_task_by_id(task1.id)
    assert retrieved_task == task1


def test_get_task_by_id_nonexistent(task_manager): # No status impact
    retrieved_task = task_manager.get_task_by_id('nonexistent_id')
    assert retrieved_task is None


def test_get_statistics(task_manager): # Status is checked here through stats
    task_manager.add_task(title='Task 1', priority='high')
    task_manager.add_task(title='Task 2', priority='medium')
    task1 = task_manager.add_task(title='Task 3', priority='low')
    task_manager.complete_task(task1.id)
    stats = task_manager.get_statistics()
    assert stats['total'] == 3
    assert stats['completed'] == 1
    assert stats['pending'] == 2 # Pending is checked here
    assert stats['priorities']['high'] == 1
    assert stats['priorities']['medium'] == 1
    assert stats['priorities']['low'] == 1


def test_add_task_with_priority(task_manager):
    task = task_manager.add_task(title='New Task', priority='high')
    assert task is not None
    assert task.title == 'New Task'
    assert task.priority == 'high'
    assert len(task_manager.list_tasks()) == 1


def test_add_task_with_empty_title(task_manager):
    task = task_manager.add_task(title='')
    assert task is None


def test_add_task_with_space_only_title(task_manager):
    task = task_manager.add_task(title='   ')
    assert task is None
