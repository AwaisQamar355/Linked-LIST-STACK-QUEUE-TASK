class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)  # Insert new data at the end
        self._bubble_up(len(self.heap) - 1)  # Maintain heap property by bubbling up

    def get_min(self):
        if self.heap:
            return self.heap[0]  # Root of the heap is the minimum element
        return None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element in the heap
        
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._bubble_down(0)  # Maintain heap property by bubbling down
        return min_element

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        # Keep bubbling up until the heap property is restored or we're at the root
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        length = len(self.heap)
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Check if the left child is smaller than the current node
        if left_child_index < length and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        # Check if the right child is smaller than the current smallest
        if right_child_index < length and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        # If the smallest element is not the current node, swap and continue bubbling down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def heapify(self):
        # Build the heap from an unsorted array by calling _bubble_down for all non-leaf nodes
        n = len(self.heap)
        for i in range((n // 2) - 1, -1, -1):
            self._bubble_down(i)


















