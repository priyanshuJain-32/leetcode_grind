class MyQueue:

    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return self.s.popleft()

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return len(self.s)==0