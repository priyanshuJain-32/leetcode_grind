class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.array = []
        while head:
            self.array.append(head.val)
            head = head.next
    def getRandom(self) -> int:
        return random.choice(self.array)