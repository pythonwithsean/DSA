import importlib.util
import pathlib
import pytest

HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("heap_impl_2", str(HERE / "../heap_impl_2.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Heap = module.Heap


def test_insert_peek_and_poll_order():
    h = Heap()
    values = [5, 1, 3, 2, 4]
    for v in values:
        h.insert(v)
    assert h.peek() == 1
    out = [h.poll() for _ in range(len(values))]
    assert out == [1, 2, 3, 4, 5]
    assert h.is_empty()


def test_insert_with_duplicates():
    h = Heap()
    for v in [2, 1, 2, 1]:
        h.insert(v)
    out = [h.poll() for _ in range(4)]
    assert out == [1, 1, 2, 2]


def test_mixed_operations_preserve_heap_property():
    h = Heap()
    h.insert(10)
    h.insert(5)
    assert h.poll() == 5
    h.insert(7)
    h.insert(3)
    out = [h.poll() for _ in range(3)]
    assert out == [3, 7, 10]


def test_peek_on_empty_returns_none():
    h = Heap()
    assert h.peek() == None


def test_poll_on_empty_returns_none():
    h = Heap()
    assert h.poll() is None


def test_insert_and_poll_large_dataset():
    h = Heap()
    values = list(range(1000, 0, -1))  # Insert 1000 to 1
    for v in values:
        h.insert(v)
    out = [h.poll() for _ in range(len(values))]
    assert out == sorted(values)


def test_heap_property_after_multiple_operations():
    h = Heap()
    h.insert(10)
    h.insert(20)
    h.insert(5)
    h.poll()
    h.insert(15)
    h.insert(2)
    assert h.poll() == 2
    assert h.poll() == 10
    assert h.poll() == 15
    assert h.poll() == 20


def test_peek_does_not_remove_element():
    h = Heap()
    h.insert(3)
    h.insert(1)
    assert h.peek() == 1
    assert h.peek() == 1  # Ensure peek doesn't remove the element
    assert h.poll() == 1
    assert h.poll() == 3
