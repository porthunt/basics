import pytest

from structures.linkedlist import LinkedList


@pytest.fixture
def linked_list():
    return LinkedList()


def ignore_size(linked_list):
    assert linked_list.size() == 0


def test_insert(linked_list):
    assert linked_list.insert(3) is True


def test_insert_unsupported(linked_list):
    with pytest.raises(AttributeError):
        linked_list.insert("abc")


def ignore_search(linked_list):
    linked_list.insert(5)
    assert linked_list.search(5) is True


def ignore_search_not_found(linked_list):
    with pytest.raises(ValueError) as e:
        linked_list.search(2)
        assert "not in list" in str(e.value)


def test_show(linked_list):
    linked_list.insert(6)
    assert str(linked_list) == "<6>"
    linked_list.insert(8)
    assert str(linked_list) == "<6, 8>"


def ignore_remove(linked_list):
    linked_list.insert(10)
    assert linked_list.remove(10) is True


def ignore_remove_not_in_list(linked_list):
    with pytest.raises(ValueError) as e:
        linked_list.search(1)
        assert "not in list" in str(e.value)
