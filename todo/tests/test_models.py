from tasks.models import Task


def test_round_trip_dict():
    task = Task(
        id=1, title="demo", done=True, created_at="2026-01-01T00:00:00+00:00"
    )
    assert Task.from_dict(task.to_dict()) == task


def test_defaults():
    task = Task(id=5, title="thing")
    assert task.done is False
    assert task.created_at
