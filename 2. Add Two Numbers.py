# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        carry = 0
        while l1 or l2 or carry!=0:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            total = d1+d2+carry
            val = (total)%10
            carry = (total)//10
            
            ans.next = ListNode(val)
            ans = ans.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
