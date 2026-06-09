import pytest

from fsm import StateMachine, TransitionError


def test_initial_state():
    sm = StateMachine("idle")
    assert sm.state == "idle"


def test_basic_transition():
    sm = StateMachine("idle")
    sm.add_transition("start", "idle", "running")
    sm.add_transition("stop", "running", "idle")
    assert sm.trigger("start") == "running"
    assert sm.state == "running"
    assert sm.trigger("stop") == "idle"


def test_undefined_event_raises():
    sm = StateMachine("idle")
    with pytest.raises(TransitionError):
        sm.trigger("nope")


def test_duplicate_transition_raises():
    sm = StateMachine("idle")
    sm.add_transition("e", "idle", "next")
    with pytest.raises(ValueError):
        sm.add_transition("e", "idle", "other")


def test_action_runs_on_transition():
    calls = []
    sm = StateMachine("a")
    sm.add_transition("go", "a", "b", action=lambda value: calls.append(value))
    sm.trigger("go", "hello")
    assert calls == ["hello"]


def test_on_enter_and_on_exit():
    events = []
    sm = StateMachine("idle")
    sm.add_transition("go", "idle", "active")
    sm.on_exit("idle", lambda: events.append("exit-idle"))
    sm.on_enter("active", lambda: events.append("enter-active"))
    sm.trigger("go")
    assert events == ["exit-idle", "enter-active"]


def test_can_trigger():
    sm = StateMachine("idle")
    sm.add_transition("go", "idle", "active")
    assert sm.can_trigger("go")
    assert not sm.can_trigger("stop")


def test_reset_returns_to_initial_state():
    sm = StateMachine("idle")
    sm.add_transition("go", "idle", "active")
    sm.trigger("go")
    sm.reset()
    assert sm.state == "idle"
