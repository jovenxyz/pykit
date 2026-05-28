# tasks

A tiny, dependency-free **command-line task manager** that stores your to-dos in
a small JSON file. Add, list, complete, remove and clear tasks from the terminal.

## Install (editable)

```bash
cd todo
pip install -e .
```

## Development

```bash
cd todo
pip install pytest
pytest
```

## Where tasks are stored

By default tasks live in `~/.local/share/tasks/tasks.json`. Override the location
with the `--file` option or the `TASKS_FILE` environment variable:

```bash
tasks --file ./my-tasks.json add "write the report"
TASKS_FILE=./my-tasks.json tasks list
```
