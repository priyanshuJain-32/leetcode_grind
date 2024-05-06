class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            if stack and temp.val>stack[-1].val:
                stack.pop()
            else:
                stack.append(temp)
                temp = temp.next
        
        if not stack:
            return

        head = ListNode(0)
        temp = head
        for node in stack:
            temp.next = node
            temp = temp.next
        temp.next = None
        return head.next