from celery.app import task
from admin_panel import tasks
from unittest.mock import patch, call


def test_task():
    assert tasks.create_task.run(1)
    assert tasks.create_task.run(2)
    assert tasks.create_task.run(3)


@patch('admin_panel.tasks.create_task.run')
def test_mock_task(mock_run):
    assert tasks.create_task.run(1)
    tasks.create_task.run.assert_called_once_with(1)

    assert tasks.create_task.run(2)
    tasks.create_task.run.call_count == 2

    assert tasks.create_task.run(3)
    tasks.create_task.run.call_count == 3
