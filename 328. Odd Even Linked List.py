class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        temp1 = even
        odd = ListNode()
        temp2 = odd
        count = 1
        while head:
            if count%2!=0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            count += 1
        even.next = None
        odd.next = temp1.next
        return temp2.next