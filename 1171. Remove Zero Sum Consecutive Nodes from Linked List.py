class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        nodePointers = {0:dummy}
        prefix = 0
        while head:
            prefix += head.val
            nodePointers[prefix] = head
            head = head.next
        
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = nodePointers[prefix].next
            head = head.next
        return dummy.next