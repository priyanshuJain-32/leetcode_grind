# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

	# Faster 280 ms
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next
        if fast:
            slow = slow.next
        print(prev, slow)
        while prev and slow:
            if prev.val!=slow.val:
                break
            prev = prev.next
            slow = slow.next
        return not prev

        # Slow 340 ms approach
        temp = head
        L = ""
        while temp:
            L += str(temp.val)
            temp = temp.next
        return L==L[::-1]