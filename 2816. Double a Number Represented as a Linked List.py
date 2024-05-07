# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            nxt = curr.next
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        head = reverse(head)
        
        temp = head
        carry,v = 0,0
        
        while temp:
            v = temp.val*2 + carry
            temp.val = v-10 if v>9 else v
            carry = 1 if v>9 else 0
            if not temp.next and carry:
                temp.next = ListNode(carry)
                break
            temp = temp.next

        head = reverse(head)

        if head.val==0 and head.next:
            return head.next

        return head