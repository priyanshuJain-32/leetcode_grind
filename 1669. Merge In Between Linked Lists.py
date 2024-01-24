class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        count = 0
        m = a-1
        n = b+1
        while list1:
            if count==m:
                point1 = list1
            elif count == n:
                point2 = list1
                break
            list1 = list1.next
            count += 1
        point1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = point2
        return temp