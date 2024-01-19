class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        total = 0
        dummy = ListNode()
        temp = dummy
        while curr.next:
            curr = curr.next
            total += curr.val
            if curr.val == 0:
                newNode = ListNode(total)
                dummy.next = newNode
                dummy = dummy.next
                total = 0
        return temp.next