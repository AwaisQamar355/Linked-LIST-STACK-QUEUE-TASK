class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queuees:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newnode = QueueNode(data)
        if self.rear:
            self.rear.next = newnode
        self.rear = newnode
        if not self.front:
            self.front = newnode

    def dequeue(self):
        if self.is_empty():
            return None
        dequeueddata = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeueddata

    def is_empty(self):
        return self.front is None









