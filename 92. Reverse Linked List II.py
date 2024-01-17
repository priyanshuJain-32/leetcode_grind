# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        L = []
        n = 1
        while temp:
            L.append(temp.val)
            if n == left:
                pointer = temp
            n += 1
            temp = temp.next

        idx = right-1
        while idx >= left - 1:
            pointer.val = L[idx]
            idx -= 1
            pointer = pointer.next
            
        return head
