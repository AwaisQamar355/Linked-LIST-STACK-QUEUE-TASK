class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newnode = StackNode(data)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.is_empty():
            return None
        poppeddata = self.top.data
        self.top = self.top.next
        return poppeddata

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None












