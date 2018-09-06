
class Node:
    """
    Class implementation for each node of the linked list.
    .. todo:: extend this to more than integer.
    """

    def __init__(self, nid: int):
        self.nid = nid
        self.pointer = None


class LinkedList:
    """
    Class that represents the LinkedList.
    .. todo:: create an args that decides if it should be ordered. Default: False.
    """

    def __init__(self):
        """
        When starting the list, the HEAD should point to None,
        and the current TAIL should point to the HEAD.
        """
        self.HEAD = None
        self.TAIL = self.HEAD

    def size(self) -> int:
        """
        Method to return the size of the list.
        :return: the size of the list (i.e. the number of elements in it) as an integer.
        """
        elements = 0
        current = self.TAIL
        while current is not None:
            elements += 1
            current = current.pointer
        return elements

    def insert(self, nid: int) -> bool:
        """
        Inserts a new element 'nid' on the list.
        :param nid: an integer that you want to add to the list.
        :return: boolean True in case the element is added to the list.
        :raise AttributeError: in case nid is not an integer.
        """
        if not isinstance(nid, int):
            raise AttributeError

        node = Node(nid)
        node.pointer = self.TAIL
        self.TAIL = node
        return True

    def remove(self, nid: int) -> bool:
        """
        Removes the element 'nid' from the list.
        :param nid: an integer that you want to remove from the list.
        :return: boolean True in case the element is added to the list.
        :raise ValueError: in case nid is not on the list.
        """
        current = self.TAIL
        last = None
        while current is not None:
            if current.nid == nid:
                if last is None:
                    self.TAIL = current.pointer
                else:
                    last.pointer = current.pointer
                    self.TAIL = last
                return True
            last = current
            current = current.pointer
        raise ValueError("{} not in list".format(nid))

    def search(self, nid: int) -> bool:
        """
        Searches for the element 'nid' on the list.
        :param nid: an integer that you want to search on the list.
        :return: boolean True in case the element was found.
        :raise ValueError: in case nid is not on the list.
        """
        current = self.TAIL
        while current is not None:
            if current.nid == nid:
                return True
            current = current.pointer
        raise ValueError("{} not in list".format(nid))

    def __str__(self):
        current = self.TAIL
        out = ""
        while current is not None:
            out += "{nid}".format(nid=current.nid)
            current = current.pointer
            out += ", " if current else ""
        return "<{out}>".format(out=out)
