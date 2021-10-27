class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack은 비어 있습니다."
        delete_node = self.head
        self.head = self.head.next
        return delete_node.data

    def peek(self):
        if self.is_empty():
            return "Stack은 비어 있습니다."
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


stack = Stack()

stack.push(1)
print(stack.is_empty())
stack.push(2)
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.is_empty())
