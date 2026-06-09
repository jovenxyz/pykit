# fsm

A tiny, dependency-free **finite state machine** with declarative
transitions, optional per-transition actions, and ``on_enter`` /
``on_exit`` hooks per state.

## Usage

```python
from fsm import StateMachine

sm = StateMachine(initial="idle")
sm.add_transition("start", "idle", "running")
sm.add_transition("stop", "running", "idle")
sm.on_enter("running", lambda: print("started!"))

sm.trigger("start")    # state -> "running"
sm.trigger("stop")     # state -> "idle"
```

States and events may be any hashable values. ``trigger`` raises
``TransitionError`` when the event is not defined from the current state.

## Tests

```bash
cd fsm
pytest
```
