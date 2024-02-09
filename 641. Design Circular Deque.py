class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.length = 0
        self.maxLength = k

    def insertFront(self, value: int) -> bool:
        if self.length == self.maxLength:
            return False
        self.deque = [value] + self.deque
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.length == self.maxLength:
            return False
        self.deque = self.deque + [value]
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        self.deque = self.deque[1:]
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        self.deque = self.deque[:-1]
        self.length -= 1
        return True

    def getFront(self) -> int:
        try:
            return self.deque[0]
        except:
            return -1

    def getRear(self) -> int:
        try:
            return self.deque[-1]
        except:
            return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.maxLength