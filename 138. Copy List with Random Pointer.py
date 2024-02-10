class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        vals = []
        temp = head
        idx = 0
        while temp:
            vals.append(temp.val)
            temp.val = idx
            temp = temp.next
            idx += 1
        
        # Create new List
        newHead = Node(0)
        newTemp = newHead
        pointerD = [0]*idx

        for i in range(len(vals)):
            newTemp.val = vals[i]
            pointerD[i] = newTemp
            if not i==len(vals)-1:
                newTemp.next = Node(0)
                newTemp = newTemp.next

        # Fix Random
        temp = head
        newTemp = newHead
        while temp:
            try:
                newTemp.random = pointerD[temp.random.val]
            except:
                newTemp.random = None
            newTemp = newTemp.next
            temp = temp.next
            
        return newHead