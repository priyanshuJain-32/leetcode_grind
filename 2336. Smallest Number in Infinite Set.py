class SmallestInfiniteSet:

    def __init__(self):
        # self.l = [i for i in range(1000,0,-1)]
        # self.mini = deque()
        # self.mini.extend(range(1,1001))
        self.mini = 1
        self.added = []
        self.popped = set()

    def popSmallest(self) -> int:
        if self.added:
            val = min(self.added)
            self.added.remove(val)
            self.popped.add(val)
            return val
        else:
            val = self.mini
            self.popped.add(val)
            self.mini+=1
            return val
        # val = self.l.pop()
        # self.popped.add(val)
        # return val

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.added.append(num)
            self.popped.remove(num)
        # if num in self.popped:
        #     self.l.append(num)
        #     self.popped.remove(num)
        #     self.l.sort(reverse=True)
        # if num in self.popped:
        #     self.mini.appendleft(num)
        #     self.popped.remove(num)
        #     self.mini = deque(sorted(self.mini))


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)