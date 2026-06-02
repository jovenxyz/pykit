# semver

A tiny, dependency-free implementation of [semantic versioning][spec]: parse
``"1.2.3-rc.1+build.5"``, compare two versions, and bump major/minor/patch.

[spec]: https://semver.org/spec/v2.0.0.html

## Usage

```python
from semver import parse

v = parse("1.2.3-rc.1")
assert (v.major, v.minor, v.patch) == (1, 2, 3)
assert v.prerelease == "rc.1"

assert parse("1.0.0-rc.1") < parse("1.0.0")
assert str(parse("1.2.3").bump_minor()) == "1.3.0"
```

Build metadata is preserved on round-trip but ignored when ordering versions,
per the spec.

## Tests

```bash
cd semver
pytest
```
