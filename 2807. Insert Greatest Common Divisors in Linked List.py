# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a, a)
        prev = head
        temp = prev.next
        while True:
            if temp==None:
                break
            val = gcd(prev.val, temp.val)
            prev.next = ListNode(val)
            prev.next.next = temp
            prev = temp
            temp = temp.next
            
        return head
