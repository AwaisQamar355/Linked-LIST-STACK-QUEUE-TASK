class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    # Create a dummy node to help with easy insertion into the merged list
    dummy_node = Node(0)
    current_merged = dummy_node

    # Step 1: Merge elements while both lists have nodes
    while current1 and current2:
        if current1.data < current2.data:
            current_merged.next = current1
            current1 = current1.next
        else:
            current_merged.next = current2
            current2 = current2.next
        current_merged = current_merged.next

    # Step 2: Append remaining elements from list1 or list2
    if current1:
        current_merged.next = current1
    elif current2:
        current_merged.next = current2

    # Return the merged linked list starting from the node after the dummy node
    merged_list.head = dummy_node.next
    return merged_list








