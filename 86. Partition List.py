class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp1, temp2 = before, after = ListNode(), ListNode()
        while head:
            if head.val>=x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next
            head = head.next
        after.next = None
        before.next = temp2.next
        head = temp1.next
        return head