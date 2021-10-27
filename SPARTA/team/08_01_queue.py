import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def push(self, value):
        new_node = Node(value)
        if self.empty():
            self.tail = new_node
            self.head = new_node
        self.tail.next = new_node
        self.tail = new_node
        return

    def pop(self):
        if self.empty():
            return print(-1)
        delete_node = self.head
        self.head = self.head.next
        return print(delete_node.data)

    def size(self):
        if self.empty():
            return print(0)
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return print(count)

    def front(self):
        if self.empty():
            return print(-1)
        return print(self.head.data)

    def back(self):
        if self.empty():
            return -1
        return print(self.tail.data)

    def empty(self):
        return self.head is None


N = int(sys.stdin.readline())
test = Queue()

for index in range(N):
    func_input = sys.stdin.readline().split()
    func_name = func_input[0]

    if func_name == "push":
        test.push(int(func_input[1]))
    elif func_name == "back":
        test.back()
    elif func_name == "size":
        test.size()
    elif func_name == "empty":
        if test.empty():
            print(1)
        else:
            print(0)
    elif func_name == "front":
        test.front()
    else:
        test.pop()
