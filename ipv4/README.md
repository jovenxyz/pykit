# ipv4

A tiny, dependency-free helper to convert IPv4 addresses between dotted-quad
strings and 32-bit unsigned integers.

## Usage

```python
from ipv4 import ip_to_int, int_to_ip

assert ip_to_int("192.168.1.1") == 0xC0A80101
assert int_to_ip(0xC0A80101) == "192.168.1.1"
```

## Tests

```bash
cd ipv4
pytest
```
