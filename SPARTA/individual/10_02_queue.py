class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            return "비어있어!"
        delete_node = self.head
        self.head = self.head.next
        return delete_node.data

    def peek(self):
        if self.is_empty():
            return "비어있어"
        return self.head.data

    def is_empty(self):
        return self.head is None


f1 = Queue()

f1.enqueue(3)
f1.enqueue(4)
f1.enqueue(5)
f1.enqueue(6)
print(f1.peek())
print(f1.dequeue())
print(f1.dequeue())
print(f1.dequeue())
print(f1.is_empty())
print(f1.dequeue())
print(f1.dequeue())
print(f1.is_empty())
print(f1.peek())