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
