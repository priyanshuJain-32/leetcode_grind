class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        nxt = head.next.next
        pos = 1
        pos_arr = []
        if not nxt:
            return [-1,-1]
        while nxt:
            if prev.val<curr.val>nxt.val or prev.val>curr.val<nxt.val:
                pos_arr.append(pos)
            prev, curr, nxt = prev.next, curr.next, nxt.next
            pos += 1
        
        n = len(pos_arr)
        minDist, maxDist = 1000000, 0        
        if n<2:
            return [-1,-1]
        else:
            for i in range(n-1):
                minDist = min(minDist, pos_arr[i+1]-pos_arr[i])
        return [minDist, pos_arr[-1]-pos_arr[0]]