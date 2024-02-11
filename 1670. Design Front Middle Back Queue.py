class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        self.length += 1

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(self.length//2, val)
        self.length += 1

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.length += 1

    def popFront(self) -> int:
        try:
            val = self.queue.pop(0)
            self.length -= 1
            return val
        except:
            return -1

    def popMiddle(self) -> int:
        try:
            val = self.queue.pop((self.length-1)//2)
            self.length -= 1
            return val
        except:
            return -1

    def popBack(self) -> int:
        try:
            val = self.queue.pop()
            self.length -= 1
            return val
        except:
            return -1