# memoize

A tiny, dependency-free **time-bounded memoization decorator**. Cache return
values for ``ttl`` seconds per unique argument combination -- handy for
short-lived lookups (DNS, config, expensive computations) without leaking
memory forever.

## Usage

```python
from memoize import memoize

@memoize(ttl=30)
def lookup_user(user_id):
    ...

lookup_user(1)       # actually runs
lookup_user(1)       # cached for 30s
lookup_user.clear()  # drop the cache
```

Pass ``time_func=`` to inject a deterministic clock in tests.

## Tests

```bash
cd memoize
pytest
```
