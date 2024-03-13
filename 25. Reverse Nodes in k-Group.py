class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
     # Convert t list and back to Linked List
        ls = []
        n = 0
        temp = head
        while head:
            ls.append(head.val)
            head = head.next
            n+=1
        
        for i in range(0,n-k+1,k):
            ls[i:i+k] = reversed(ls[i:i+k])
        dummy = temp
        i = 0
        while temp:
            temp.val = ls[i]
            temp = temp.next
            i+=1
        return dummy