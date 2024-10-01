class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


def is_balanced(expression: str) -> bool:
    stack = Stack()
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != matching_parentheses[char]:
                return False

    return stack.is_empty()














