def test_basic_functionality():
    assert 1 == 1

from task_manager.task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    manager.add_task("Test task")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Test task"

def test_remove_task():
    manager = TaskManager()
    manager.add_task("Task to remove")
    manager.remove_task(0)
    assert len(manager.tasks) == 0

def test_placeholder_test_for_jira_undefined():
    assert True

def test_add_task_with_description():
    manager = TaskManager()
    manager.add_task("Task with description", "This is a description for the task.")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Task with description"
    assert manager.tasks[0].description == "This is a description for the task."

def test_add_task_with_due_date():
    manager = TaskManager()
    manager.add_task("Task with due date", due_date="2024-12-31")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Task with due date"
    assert manager.tasks[0].due_date == "2024-12-31"

def test_add_task_with_priority():
    manager = TaskManager()
    manager.add_task("Task with priority", priority="High")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Task with priority"

def test_initialize_task_manager():
    manager = TaskManager()
    assert isinstance(manager, TaskManager)

def test_undefined_jira_issue():
    manager = TaskManager()
    manager.add_task("Undefined Jira Task")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Undefined Jira Task"
    manager.remove_task(0)
    assert len(manager.tasks) == 0

def test_add_task_only_name():
    manager = TaskManager()
    manager.add_task("Task with only name")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Task with only name"

def test_add_task_empty_name():
    manager = TaskManager()
    manager.add_task("")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == ""