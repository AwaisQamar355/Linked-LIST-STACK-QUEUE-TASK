class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

def reverse_first_k_elements(queue: Queue, k: int) -> Queue:
    if queue.is_empty() or k <= 0 or k > queue.size():
        return queue

    stack = []

    # Step 1: Dequeue first k elements and push them to the stack
    for _ in range(k):
        stack.append(queue.dequeue())

    # Step 2: Pop from the stack and enqueue back to the queue (reverses order)
    while stack:
        queue.enqueue(stack.pop())

    # Step 3: Move the remaining elements to the back of the queue
    size = queue.size()
    for _ in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue








