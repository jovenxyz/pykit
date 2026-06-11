# cron

A tiny, dependency-free **cron expression** parser and matcher. Parse a
classic 5-field cron line (``minute hour day month weekday``) and check
whether a ``datetime`` would trigger the schedule.

## Usage

```python
from datetime import datetime

from cron import matches

# Every 5 minutes:
assert matches("*/5 * * * *", datetime(2026, 6, 15, 9, 5))

# 9 AM on weekdays:
assert matches("0 9 * * 1-5", datetime(2026, 6, 15, 9, 0))   # Monday
```

Supports lists (``0,15,30,45``), ranges (``1-5``), wildcards (``*``) and
steps (``*/5`` or ``0-30/10``). Weekdays use the cron convention: Sunday
is 0 and Saturday is 6.

## Tests

```bash
cd cron
pytest
```
