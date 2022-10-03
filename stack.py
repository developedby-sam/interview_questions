class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"[value: {self.value} next: {self.next}]"


class Stack:
    # CONSTRUCTOR
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return f"top: {self.top} \nbottom: {self.bottom} \nlength: {self.length}"

    # GET THE TOPMOST ITEM
    def peek(self):
        return self.top

    # ADD ITEM TO THE STACK
    def push(self, value):
        new_node = Node(value)

        if not self.length:
            self.bottom = new_node
            self.top = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer

        self.length += 1

        return self

    def pop(self):
        if not self.top:
            return None

        if self.length == 1:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1


num_stack = Stack()
print(num_stack.peek())
num_stack.push('google')
num_stack.push('udemy')
num_stack.push('discord')
num_stack.pop()
num_stack.pop()
num_stack.pop()
print(num_stack)
