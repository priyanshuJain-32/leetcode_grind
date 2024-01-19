class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next
        max_sum = 0
        while prev and slow:
            max_sum = max(max_sum, prev.val+slow.val)
            prev, slow = prev.next, slow.next
        return max_sum