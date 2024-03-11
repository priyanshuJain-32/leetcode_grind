class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple.sort()
        capacity.sort()
        i = len(apple) -1 
        j = len(capacity)-1
        used_j = False
        count = 1
        while i>-1:
            capacity[j], apple[i] = max(0,capacity[j]-apple[i]), max(0, apple[i]-capacity[j])
            used_j = True
            print(apple, capacity)
            if capacity[0]==0:
                break
            if apple[i]==0:
                i-=1
            if capacity[j]==0:
                count += 1
                j-=1
                used_j = False
        return count if used_j else count-1
            