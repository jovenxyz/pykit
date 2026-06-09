"""A small declarative finite state machine."""
from __future__ import annotations

from typing import Callable, Dict, Hashable, Optional, Tuple


class TransitionError(ValueError):
    """Raised when a triggered event has no transition from the current state."""


class StateMachine:
    """A simple deterministic state machine.

    States and events may be any hashable values. Each transition can have
    an optional ``action`` callable invoked on a successful transition.
    """

    def __init__(self, initial: Hashable) -> None:
        self._initial = initial
        self._state = initial
        self._transitions: Dict[
            Tuple[Hashable, Hashable], Tuple[Hashable, Optional[Callable]]
        ] = {}
        self._on_enter: Dict[Hashable, Callable] = {}
        self._on_exit: Dict[Hashable, Callable] = {}

    @property
    def state(self) -> Hashable:
        return self._state

    def add_transition(
        self,
        event: Hashable,
        source: Hashable,
        target: Hashable,
        action: Optional[Callable] = None,
    ) -> None:
        """Register a transition: ``event`` from ``source`` moves to ``target``."""
        key = (source, event)
        if key in self._transitions:
            raise ValueError(f"transition already defined: {key}")
        self._transitions[key] = (target, action)

    def on_enter(self, state: Hashable, callback: Callable) -> None:
        """Run ``callback`` when entering ``state``."""
        self._on_enter[state] = callback

    def on_exit(self, state: Hashable, callback: Callable) -> None:
        """Run ``callback`` just before leaving ``state``."""
        self._on_exit[state] = callback

    def can_trigger(self, event: Hashable) -> bool:
        """Return ``True`` if ``event`` is valid from the current state."""
        return (self._state, event) in self._transitions

    def trigger(self, event: Hashable, *args, **kwargs) -> Hashable:
        """Fire ``event``; return the new state."""
        key = (self._state, event)
        if key not in self._transitions:
            raise TransitionError(
                f"no transition for event {event!r} from state {self._state!r}"
            )
        target, action = self._transitions[key]
        if self._state in self._on_exit:
            self._on_exit[self._state](*args, **kwargs)
        if action is not None:
            action(*args, **kwargs)
        self._state = target
        if target in self._on_enter:
            self._on_enter[target](*args, **kwargs)
        return target

    def reset(self) -> None:
        """Return the machine to its initial state (no callbacks run)."""
        self._state = self._initial
