from calc.cli import main


def test_cli_evaluates_expression(capsys):
    exit_code = main(["2 + 3 * 4"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "14"


def test_cli_reports_errors(capsys):
    exit_code = main(["1 / 0"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "error" in captured.err.lower()
