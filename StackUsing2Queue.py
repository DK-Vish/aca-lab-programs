class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            raise IndexError("Stack is empty.")
        return self.q1.pop(0)

    def top(self):
        if self.empty():
            raise IndexError("stack is emoty.")
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

stack = MyStack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())    # Output: 30
print(stack.pop())    # Output: 30
print(stack.top())    # Output: 20
print(stack.empty())  # Output: False
print(stack.pop())    # Output: 20
print(stack.pop())    # Output: 10
print(stack.empty())

