import collections


class MyQueue:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.popleft()

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return False if self.q else True


obj = MyQueue()
obj.push(1)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()

print(param_3)
print(param_2)
print(param_4)