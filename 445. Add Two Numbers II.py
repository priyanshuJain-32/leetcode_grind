class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        while l1:
            num1 *= 10
            num1 += l1.val
            l1 = l1.next
        while l2:
            num2 *= 10
            num2 += l2.val
            l2 = l2.next
        ret = ListNode()
        temp = ret
        res = str(num1+num2)
        for i in range(len(res)):
            ret.val = int(res[i])
            if i==len(res)-1:
                break
            ret.next = ListNode()
            ret = ret.next
        return temp