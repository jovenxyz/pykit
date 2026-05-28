"""Allow ``python -m csvjson`` to run the CLI."""
from csvjson.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
