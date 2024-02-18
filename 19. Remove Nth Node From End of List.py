class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        m = 0
        while temp:
            temp = temp.next
            m += 1
        if m==1:
            return None
        elif m==n:
            return head.next
        count = 0
        temp = head
        pointer = temp
        while m-count>n:
            pointer = temp
            temp = temp.next
            count += 1
        pointer.next = pointer.next.next if pointer.next else None
        return head