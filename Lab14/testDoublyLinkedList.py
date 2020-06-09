class Node:

    def __init__(self, item):
        self.mItem = item
        self.mNext = None
        self.mPrev = None

class DoublyLinkedList:

    def __init__(self):
        self.mFirst = None
        self.mLast = None
        self.mCurr = None

    def empty(self):
        return self.mFirst is None

    def setFirst(self):
        self.mCurr = self.mFirst
    def setLast(self):
        self.mCurr = self.mLast

    def next(self):
        if self.mCurr != self.mLast:
            self.mCurr = self.mCurr.mNext

    def prev(self):
        if self.mCurr != self.mFirst:
            self.mCurr = self.mCurr.mPrev

    def current(self):
        if self.mCurr is not None:
            return self.mCurr.mItem
        else:
            return None

    def insertBefore(self, item):
        node = Node(item)
        node.mNext = self.mCurr
        if self.empty():
            self.mCurr = self.mFirst = self.mLast = node
        else:
            if self.mCurr == self.mFirst:
                self.mFirst = node
            else:
                node.mPrev = self.mCurr.mPrev
                self.mCurr.mPrev.next = node
        self.mCurr.mPrev = node

    def insertAfter(self, item):
        node = Node(item)
        node.mPrev = self.mCurr
        if self.empty():
            self.mCurr = self.mFirst = self.mLast = node
        else:
            if self.mCurr == self.mLast:
                self.mLast = node
            else:
                node.mNext = self.mCurr.mNext
                self.mCurr.mNext.prev = node
        self.mCurr.mNext = node
        self.mCurr = node

    def remove(self):
        if self.epmty():
            raise Exception("dfdfd")
        node = self.mCurr

        if node == self.mFirst:
            self.mFirst = node.mNext
        else:
            node.mPrev.mNext = node.mNext

        if node == self.mLast:
            self.mCurr = self.mLast = node.mPrev
        else:
            node.mNext.mPrev = node.mPrev
            self.mCurr = node.mNext
        del node
    def __str__(self):
        return str(self.current())

dl = DoublyLinkedList()

dl.insertBefore(33)
dl.insertBefore(0)
dl.insertBefore(30003)
dl.insertBefore(3)
dl.insertBefore(20)
print(dl)
dl.prev()
print(dl)

