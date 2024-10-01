class doublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        newnode = doublyNode(data)
        if self.head:
            self.head.prev = newnode
        newnode.next = self.head
        self.head = newnode

    def insert_at_tail(self, data):
        newnode = doublyNode(data)
        if not self.head:
            self.head = newnode
            return
        curren = self.head
        while curren.next:
            curren = curren.next
        curren.next = newnode
        newnode.prev = curren

    def delete_node(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        curren = self.head
        while curren and curren.data != value:
            curren = curren.next
        if curren:
            if curren.next:
                curren.next.prev = curren.prev
            if curren.prev:
                curren.prev.next = curren.next

    def search(self, value):
        curren = self.head
        while curren:
            if curren.data == value:
                return True
            curren = curren.next
        return False

    def reverse(self):
        curren = self.head
        prev = None
        while curren:
            prev = curren.prev
            curren.prev = curren.next
            curren.next = prev
            curren = curren.prev
        if prev:
            self.head = prev.prev











