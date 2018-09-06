import pytest

from structures.linkedlist import LinkedList


@pytest.fixture
def linked_list():
    return LinkedList()


def test_size(linked_list):
    assert linked_list.size() == 0
    linked_list.insert(3)
    assert linked_list.size() == 1


def test_insert(linked_list):
    assert linked_list.insert(3) is True


def test_insert_unsupported(linked_list):
    with pytest.raises(AttributeError):
        linked_list.insert("abc")


def test_search(linked_list):
    linked_list.insert(5)
    assert linked_list.search(5) is True


def test_search_not_found(linked_list):
    with pytest.raises(ValueError) as e:
        linked_list.search(2)
        assert "not in list" in str(e.value)


def test_search_empty(linked_list):
    with pytest.raises(ValueError) as e:
        linked_list.search(1)
        assert "not in list" in str(e.value)


def test_search_first(linked_list):
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(9)
    assert linked_list.search(3) is True


def test_search_last(linked_list):
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(9)
    assert linked_list.search(9) is True


def test_str(linked_list):
    linked_list.insert(6)
    assert str(linked_list) == "<6>"
    linked_list.insert(8)
    assert str(linked_list) == "<8, 6>"
    linked_list.insert(10)
    assert str(linked_list) == "<10, 8, 6>"


def test_remove(linked_list):
    linked_list.insert(10)
    assert linked_list.remove(10) is True


def test_remove_not_in_list(linked_list):
    with pytest.raises(ValueError) as e:
        linked_list.search(1)
        assert "not in list" in str(e.value)


def test_remove_many(linked_list):
    assert linked_list.insert(1) is True
    assert linked_list.insert(2) is True
    assert linked_list.insert(3) is True
    assert linked_list.remove(2) is True
    assert linked_list.remove(1) is True
    assert linked_list.remove(3) is True
