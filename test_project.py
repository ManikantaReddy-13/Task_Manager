# Importing functions to be tested from project.py
from project import add_task, list_tasks, complete_task

# Test for adding a task
def test_add_task():
    task_list = []
    add_task(task_list, "Buy groceries")
    assert len(task_list) == 1
    assert task_list[0]["description"] == "Buy groceries"
    assert task_list[0]["completed"] is False

# Test for listing tasks
def test_list_tasks(capsys):
    task_list = [{"description": "Finish homework", "completed": False}]
    list_tasks(task_list)
    captured = capsys.readouterr()
    assert "Tasks:" in captured.out
    assert "1. Finish homework - Not Completed" in captured.out

# Test for completing a task
def test_complete_task():
    task_list = [{"description": "Read book", "completed": False}]
    complete_task(task_list, 1)
    assert task_list[0]["completed"] is True
