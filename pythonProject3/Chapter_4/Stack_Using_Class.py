class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def pop(self):
        return None if self.is_empty() else self.stack.pop()