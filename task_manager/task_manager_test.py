def test_basic_functionality():
    assert 1 == 1

from task_manager.task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    manager.add_task("Test task")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Test task"