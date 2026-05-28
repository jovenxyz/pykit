# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Task model with JSON serialization.
- JSON-backed storage with a graceful fallback for a missing file.
- TaskManager supporting add, list, complete, remove and clear-completed.
- A `tasks` CLI with `add`, `list`, `done`, `remove` and `clear` commands.
- A `python -m tasks` entry point.
- pytest suite and GitHub Actions CI.
