class Node:

    def __init__(self, item):
        self.mItem = item
        self.mNext = None

class CircularLinkedList:
    def __init__(self):
        self.mCurr = None

    def empty(self):
        return self.mCurr is None

    def next(self):
        if self.empty():
            raise StopIteration
        else:
            self.mCurr = self.mCurr.mNext

    def current(self):
        if self.empty():
            return None
        else:
            return self.mCurr.mItem

    def insert(self, item):
        node = Node(item)
        if self.empty():
            node.mNext = node
            self.mCurr = node
        else:
            node.mNext = self.mCurr.mNext
            self.mCurr.mNext = node

    def __str__(self):
        return str(self.current())
