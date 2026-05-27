"""Allow ``python -m calc`` to run the CLI."""
from calc.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
