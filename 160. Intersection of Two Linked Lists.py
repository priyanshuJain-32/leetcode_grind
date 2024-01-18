class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Fast O(m+n)
        tempA = headA
        tempB = headB
        while tempA!=tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA

        # Slow O(n^2)
        while headA:
            temp = headB
            while temp:
                if headA==temp:
                    return headA
                temp = temp.next
            headA = headA.next
        
        return None