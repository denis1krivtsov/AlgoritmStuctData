class Node:

    def __init__(self, item):
        self.mItem = item
        self.mNext = None

class ListWithCurrent:

    def __init__(self):
        self.mHead = None
        self.mCurr = None


    def empty(self):
        return self.mHead is None

    def reset(self):
        self.mCurr = self.mHead

    def next(self):
        if self.empty() or self.mCurr.mNext is None:
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
            self.mHead = self.mCurr = node
        else:
            node.mNext = self.mCurr.mNext
            self.mCurr.mNext = node

    def __str__(self):
        return str(self.current())

    def __iter__(self):
        return ListIteration(self)

    def ReorderList(self):
        lst = []
        for el in self:
            lst.append(el)
        st = lst[1:] + lst[:1]
        st.reverse()
        new = []
        n = len(st)
        j = 0
        for i in range(n):
            if i % 2 == 0:
                new.append(st[j])
            else:
                new.append(st[n - j - 1])
                j += 1
        return new

    def Print(self):
        print(*self.ReorderList())


class ListIteration:
    def __init__(self, lst):
        self.mCursor = lst.mHead

    def __next__(self):
        if self.mCursor is None:
            raise StopIteration
        else:
            curr = self.mCursor.mItem
            self.mCursor = self.mCursor.mNext
            return curr



L = ListWithCurrent()
n = int(input())
elem = list(map(int, input().split()))
for el in elem:
    L.insert(el)
L.Print()
