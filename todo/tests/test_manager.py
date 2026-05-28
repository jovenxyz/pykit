from tasks.manager import TaskManager


def _manager(tmp_path):
    return TaskManager(tmp_path / "tasks.json")


def test_add_assigns_incrementing_ids(tmp_path):
    manager = _manager(tmp_path)
    first = manager.add("write tests")
    second = manager.add("ship it")
    assert (first.id, second.id) == (1, 2)
    assert [task.title for task in manager.list()] == ["write tests", "ship it"]
