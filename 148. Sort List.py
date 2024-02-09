class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        temp = head
        for i in arr:
            temp.val = i
            temp = temp.next
        return head