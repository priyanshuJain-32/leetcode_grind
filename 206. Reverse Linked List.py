class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        # My first solution
        if not head or not head.next:
            return head
        curr = head
        prevNewNode = ListNode(curr.val)
        while curr.next:
            curr = curr.next
            newNode = ListNode(curr.val)
            newNode.next = prevNewNode
            prevNewNode = newNode
        return prevNewNode