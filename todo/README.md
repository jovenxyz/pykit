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

## Commands

```bash
$ tasks add "write the report"
added #1: write the report
$ tasks add "review the PR"
added #2: review the PR
$ tasks done 1
completed #1: write the report
$ tasks list
[x] #1 write the report
[ ] #2 review the PR
$ tasks clear
cleared 1 completed task(s)
```
