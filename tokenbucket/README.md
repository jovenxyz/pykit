# tokenbucket

A tiny, dependency-free **token-bucket rate limiter**. Tokens refill at a
constant rate up to a fixed capacity; each event consumes one (or more)
tokens, and ``consume`` returns ``False`` instead of blocking when the
bucket is empty.

## Usage

```python
from tokenbucket import TokenBucket

bucket = TokenBucket(rate=10, capacity=5)    # 10/sec, burst up to 5

if bucket.consume():
    do_request()
else:
    print(f"backed off; retry in {bucket.wait_time():.2f}s")
```

Pass ``time_func=`` to inject a deterministic clock in tests.

## Tests

```bash
cd tokenbucket
pytest
```
