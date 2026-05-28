from tasks.models import Task
from tasks.storage import load_tasks, save_tasks


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "tasks.json"
    save_tasks(path, [Task(id=1, title="alpha"), Task(id=2, title="beta", done=True)])
    loaded = load_tasks(path)
    assert [task.title for task in loaded] == ["alpha", "beta"]
    assert loaded[1].done is True


def test_load_missing_file_returns_empty(tmp_path):
    assert load_tasks(tmp_path / "absent.json") == []
