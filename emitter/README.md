# emitter

A tiny, dependency-free **event emitter** / pubsub for synchronous
in-process events. Subscribe handlers to named events, emit values to all
of them, and unsubscribe via a returned callback or via ``off``.

## Usage

```python
from emitter import EventEmitter

ee = EventEmitter()

received = []
unsubscribe = ee.on("data", received.append)
ee.emit("data", 42)

ee.once("ready", lambda: print("ready, once only"))

unsubscribe()        # remove the "data" handler
```

Handlers receive whatever positional and keyword arguments are passed to
``emit``. Removing a handler during dispatch is safe -- the current emit
still sees the handlers that were subscribed when it started.

## Tests

```bash
cd emitter
pytest
```
