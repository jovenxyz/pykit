# Contributing

Thanks for your interest in improving pytoolkit!

## Ground rules

1. Keep implementations dependency-free (standard library only).
2. Every new function or class ships with `pytest` coverage.
3. Run the suite before opening a pull request:

   ```bash
   pytest
   ```

4. Follow the existing module layout under `src/pytoolkit/`.

## Commit messages

We loosely follow [Conventional Commits](https://www.conventionalcommits.org/):
`feat:`, `fix:`, `test:`, `docs:`, `chore:`, `ci:`, `build:`.
