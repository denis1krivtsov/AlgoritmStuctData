class Stack:
    def __init__(self):
        self.items = []
    def empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]

def brackerChecker(bracker_sequence):
    stack = Stack()
    for bracker in bracker_sequence:
        if bracker == "(" or bracker == "[":
            stack.push(bracker)
        elif bracker == ")":
            if stack.empty():
                return False
            elif stack.top() != "(":
                return False
            else:
                stack.pop()
        else:
            if stack.empty():
                return False
            elif stack.top() != "[":
                return False
            else:
                stack.pop()

    if stack.empty():
        return True
    return False

def perm(lst, st, n):
    k = len(lst)
    if k == n:
        if brackerChecker("".join(lst)):
            print("".join(lst))
        return

    for el in st:
        lst_next = lst[:]
        lst_next.append(el)
        perm(lst_next, st, n)

st = ["(", ")", "[", "]"]
n = int(input())
perm([], st, n)