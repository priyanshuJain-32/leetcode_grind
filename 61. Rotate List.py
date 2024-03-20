class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head:
            return head
        
        # Calculate length of list
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n+=1
        if n==1 or k%n==0:
            return head

        # Calculate steps to traverse
        step = n-k%n-1
        temp = head
        while step>0:
            temp = temp.next
            step-=1

        # Fix the new head
        new_head = temp.next

        # Remove pointer from prev slice to next slice
        temp.next = None

        # Reach end of the slice just created
        new_temp = new_head
        while new_temp.next:
            new_temp = new_temp.next
        
        # Point the end to the previous head
        new_temp.next = head
        
        # Return new head
        return new_head