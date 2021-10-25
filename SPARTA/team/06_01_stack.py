import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    def pop(self):
        if self.head is None:
            return print(-1)
        temp = self.head
        self.head = self.head.next
        return print(temp.data)

    def size(self):
        count = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            count += 1
        return print(count)

    def empty(self):
        if self.head is None:
            print(1)
            return True
        else:
            print(0)
            return False

    def top(self):
        if self.head is None:
            return print(-1)
        return print(self.head.data)


N = int(sys.stdin.readline())
test = Stack()

for index in range(N):
    func_input = sys.stdin.readline().split()
    func_name = func_input[0]

    if func_name == "push":
        test.push(int(func_input[1]))
    elif func_name == "top":
        test.top()
    elif func_name == "size":
        test.size()
    elif func_name == "empty":
        test.empty()
    else:
        test.pop()