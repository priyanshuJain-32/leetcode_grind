# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow and fast horse approach
        slow_horse = head
        fast_horse = head
        while fast_horse and fast_horse.next:
            slow_horse = slow_horse.next
            fast_horse = fast_horse.next.next
        return slow_horse

        # My beginner solution
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1
        temp = head
        middle = n//2 + 1
        m = 1
        while temp:
            if m==middle:
                return temp
            temp = temp.next
            m += 1