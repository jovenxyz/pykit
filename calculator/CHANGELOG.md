# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Tokenizer for numbers, `+ - * / % **`, and parentheses.
- Recursive-descent parser with correct precedence and right-associative `**`.
- AST evaluator with division- and modulo-by-zero guards.
- An `evaluate()` API, a `calc` CLI, and a `python -m calc` entry point.
- pytest suite and GitHub Actions CI.
