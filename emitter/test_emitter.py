from emitter import EventEmitter


def test_basic_emit():
    ee = EventEmitter()
    received = []
    ee.on("greet", received.append)
    ee.emit("greet", "hello")
    assert received == ["hello"]


def test_multiple_subscribers_get_called():
    ee = EventEmitter()
    a, b = [], []
    ee.on("data", a.append)
    ee.on("data", b.append)
    count = ee.emit("data", 42)
    assert a == [42]
    assert b == [42]
    assert count == 2


def test_unsubscribe_with_off():
    ee = EventEmitter()
    received = []
    ee.on("ping", received.append)
    ee.off("ping", received.append)
    ee.emit("ping", 1)
    assert received == []


def test_returned_unsubscribe_callback():
    ee = EventEmitter()
    received = []

    def handler(value):
        received.append(value)

    unsubscribe = ee.on("ping", handler)
    ee.emit("ping", 1)
    unsubscribe()
    ee.emit("ping", 2)
    assert received == [1]


def test_once_only_fires_one_time():
    ee = EventEmitter()
    received = []
    ee.once("once", received.append)
    ee.emit("once", 1)
    ee.emit("once", 2)
    assert received == [1]
    assert ee.listeners("once") == []


def test_kwargs_and_positional_args():
    ee = EventEmitter()
    received = []

    def handler(a, b=None):
        received.append((a, b))

    ee.on("call", handler)
    ee.emit("call", 1, b=2)
    assert received == [(1, 2)]


def test_emit_unknown_event_is_safe():
    ee = EventEmitter()
    assert ee.emit("nope") == 0


def test_handlers_can_unsubscribe_during_dispatch():
    ee = EventEmitter()
    called = []

    def first():
        called.append("first")
        ee.off("e", second)

    def second():
        called.append("second")

    ee.on("e", first)
    ee.on("e", second)
    ee.emit("e")
    # ``emit`` copies the handler list, so ``second`` still runs once here.
    assert called == ["first", "second"]
    called.clear()
    ee.emit("e")
    assert called == ["first"]
