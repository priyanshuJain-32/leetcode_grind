class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev_n = ListNode()
        curr_n, next_n = head, head.next
        head = prev_n
        while next_n and next_n.next:
            prev_n.next, curr_n.next, next_n.next = next_n, next_n.next, curr_n
            prev_n, curr_n, next_n = curr_n, curr_n.next, curr_n.next.next
        if curr_n.next:
            prev_n.next, curr_n.next, next_n.next = next_n, next_n.next, curr_n
        return head.next