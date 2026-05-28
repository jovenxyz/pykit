"""Allow ``python -m tasks`` to run the CLI."""
from tasks.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
