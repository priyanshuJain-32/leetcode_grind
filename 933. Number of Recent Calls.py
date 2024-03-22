class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.l = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.l += 1
        while self.q[0]<t-3000:
            self.q.popleft()
            self.l-=1
        return self.l