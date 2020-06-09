class Node:

    def __init__(self, item):
        self.mItem = item
        self.mNext = None

class LinkedList:

    def __init__(self):
        self.mFirst = None

    def empty(self):
        return self.mFirst is None

    def insert(self, item):
        node = Node(item)
        node.mNext = self.mFirst
        self.mFirst = node

    def head(self):
        if self.empty():
            return None
        else:
            return self.mFirst.mItem

    def tail(self):
        if self.empty():
            raise Exception("dsf")
        self.mFirst = self.mFirst.mNext
        return self

if __name__ == "__main__":
    LL = LinkedList()
    LL.insert(55)
    LL.insert(76)
    LL.insert(5)
    print(LL.head())
    LL.tail()
    print(LL.head())
