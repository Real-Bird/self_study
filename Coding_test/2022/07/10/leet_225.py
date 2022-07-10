class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return False if len(self.stack) else True


obj = MyStack()
obj.push(1)
obj.push(2)
param_3 = obj.top()
param_2 = obj.pop()
param_4 = obj.empty()

print(param_2, param_3, param_4)