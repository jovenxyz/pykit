# retry

A tiny, dependency-free **retry decorator** with exponential backoff and
optional jitter. Wrap flaky operations -- HTTP calls, file locks, transient
errors -- in a few extra lines.

## Usage

```python
from retry import retry

@retry(attempts=5, delay=0.1, backoff=2.0, exceptions=(ConnectionError,))
def fetch_data():
    ...
```

The default is 3 attempts with no delay, retrying any ``Exception``. Pass
``sleep=`` to inject a fake sleep in tests:

```python
calls = []
decorated = retry(attempts=3, delay=0.1, sleep=calls.append)(my_func)
```

## Tests

```bash
cd retry
pytest
```
