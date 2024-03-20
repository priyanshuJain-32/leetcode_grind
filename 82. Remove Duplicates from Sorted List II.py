class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        l = []
        seen = set()
        temp = head
        while temp:
            if temp.val not in seen:
                seen.add(temp.val)
                l.append(temp.val)
            elif temp.val in seen:
                if l and l[-1]==temp.val:
                    l.pop()
            temp = temp.next
        if not l:
            return None
        temp = head
        for i in l[:-1]:
            temp.val = i
            temp = temp.next
        temp.val = l[-1]
        temp.next = None
        return head
        # if not head or not head.next:
        #     return head
        # prev = ListNode()
        # temp = prev
        # curr = head
        # nxt = head.next
        # flag = False
        # while curr and curr.next:
        #     if curr.val == nxt.val:
        #         flag = True
        #     else:
        #         if not flag:
        #             prev.next = curr
        #             prev = prev.next
        #     curr = curr.next
        #     nxt = nxt.next
        # return temp