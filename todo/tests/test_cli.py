from tasks.cli import main


def _file(tmp_path):
    return ["--file", str(tmp_path / "tasks.json")]


def test_add_and_list(tmp_path, capsys):
    args = _file(tmp_path)
    assert main(args + ["add", "buy milk"]) == 0
    capsys.readouterr()
    assert main(args + ["list"]) == 0
    out = capsys.readouterr().out
    assert "[ ] #1 buy milk" in out


def test_done_marks_complete(tmp_path, capsys):
    args = _file(tmp_path)
    main(args + ["add", "task a"])
    capsys.readouterr()
    assert main(args + ["done", "1"]) == 0
    capsys.readouterr()
    main(args + ["list"])
    assert "[x] #1 task a" in capsys.readouterr().out
