class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def appendleft(self, item):

        node = Node(item)
        node.next = self.front
        if not self.empty():
            self.front.prev = node
        else:
            self.back = node
        self.front = node

    def popleft(self):

        if self.empty():
            raise Exception("dfd")
        node = self.front
        item = node.item
        self.front = node.next
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None

        del node
        return item

    def append(self, item):
        node = Node(item)
        node.prev = self.back
        if not self.empty():
            self.back.next = node
        else:
            self.front = node
        self.back = node

    def pop(self):
        if self.empty():
            raise Exception("sdsd")
        node = self.back
        item = node.item
        self.back = node.prev
        if self.back is None:
            self.front = None
        else:
            self.back.next = None
        del node
        return item

    def __del__(self):
        while self.front is not None:
            node = self.front
            self.front = self.front.next
            del node
        self.back = None

deq = Deque()
deq.appendleft(57)
deq.append(7)
deq.appendleft(60)
print(deq.popleft())
print(deq.pop())

