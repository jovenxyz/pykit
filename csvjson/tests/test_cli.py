from csvjson.cli import main


def test_cli_csv_to_json(tmp_path, capsys):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("name,age\nalice,30\n", encoding="utf-8")
    assert main([str(csv_path), "--to", "json"]) == 0
    out = capsys.readouterr().out
    assert '"name": "alice"' in out
    assert '"age": "30"' in out


def test_cli_infers_format_from_extension(tmp_path, capsys):
    json_path = tmp_path / "data.json"
    json_path.write_text('[{"name": "alice", "age": "30"}]', encoding="utf-8")
    assert main([str(json_path)]) == 0
    out = capsys.readouterr().out
    assert "name,age" in out
    assert "alice,30" in out
