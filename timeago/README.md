# timeago

A tiny, dependency-free helper to render a ``datetime`` or unix timestamp as
a human-readable phrase like ``"2 minutes ago"`` or ``"in 3 hours"``.

## Usage

```python
from datetime import datetime, timedelta, timezone

from timeago import time_ago

now = datetime.now(timezone.utc)
assert time_ago(now - timedelta(seconds=120), now=now) == "2 minutes ago"
assert time_ago(now + timedelta(hours=3), now=now) == "in 3 hours"
```

Naive ``datetime`` inputs are treated as UTC. Unix timestamps (``int`` /
``float``) are accepted as a shortcut. Pass ``now=`` to make the result
deterministic in tests.

## Tests

```bash
cd timeago
pytest
```
