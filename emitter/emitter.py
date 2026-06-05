"""A tiny synchronous in-process event emitter / pubsub."""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable, Dict, List

Handler = Callable[..., Any]


class EventEmitter:
    """Subscribe handlers to named events and emit values to them."""

    def __init__(self) -> None:
        self._handlers: Dict[str, List[Handler]] = defaultdict(list)

    def on(self, event: str, handler: Handler) -> Callable[[], None]:
        """Subscribe ``handler`` to ``event``. Returns an unsubscribe callback."""
        self._handlers[event].append(handler)

        def unsubscribe() -> None:
            self.off(event, handler)

        return unsubscribe

    def once(self, event: str, handler: Handler) -> Callable[[], None]:
        """Subscribe a one-shot handler that auto-removes after firing."""

        def wrapper(*args, **kwargs):
            self.off(event, wrapper)
            handler(*args, **kwargs)

        return self.on(event, wrapper)

    def off(self, event: str, handler: Handler) -> None:
        """Remove ``handler`` from ``event`` (no-op if absent)."""
        handlers = self._handlers.get(event)
        if not handlers:
            return
        try:
            handlers.remove(handler)
        except ValueError:
            pass

    def emit(self, event: str, *args, **kwargs) -> int:
        """Call every handler subscribed to ``event``; return the count."""
        # Copy so handlers can unsubscribe themselves during dispatch.
        handlers = list(self._handlers.get(event, ()))
        for handler in handlers:
            handler(*args, **kwargs)
        return len(handlers)

    def listeners(self, event: str) -> List[Handler]:
        """Return a copy of the handlers subscribed to ``event``."""
        return list(self._handlers.get(event, ()))
