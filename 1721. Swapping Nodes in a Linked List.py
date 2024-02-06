class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        n = 0
        while head:
            if n==k-1:
                point1 = head
            head = head.next
            n += 1
        count = 0
        head = temp
        while head:
            if count == n-k:
                point2 = head
                break
            head = head.next
            count += 1
            
        point1.val, point2.val = point2.val, point1.val
        return temp