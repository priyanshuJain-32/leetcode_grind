# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev = head
        while temp:
            if temp.val==val:
                prev.next = temp.next
                temp = temp.next
                continue
            prev = temp
            temp = temp.next
        return head.next if head and head.val==val else head