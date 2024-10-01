class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        newnode = SingleNode(data)
        newnode.next = self.head
        self.head = newnode

    def insert_at_tail(self, data):
        newnode = SingleNode(data)
        if not self.head:
            self.head = newnode
            return
        curren = self.head
        while curren.next:
            curren = curren.next
        curren.next = newnode

    def delete_node(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        curren = self.head
        while curren.next and curren.next.data != value:
            curren = curren.next
        if curren.next:
            curren.next = curren.next.next

    def search(self, value):
        curren = self.head
        while curren:
            if curren.data == value:
                return True
            curren = curren.next
        return False

    def reverse(self):
        prev = None
        curren = self.head
        while curren:
            next_node = curren.next
            curren.next = prev
            prev = curren
            curren = next_node
        self.head = prev
