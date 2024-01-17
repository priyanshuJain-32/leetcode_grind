class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pref = [0]*n
        suff = [0]*n
        left_count = 0
        for i in range(1,n):
            pref[i] = pref[i-1]+int(boxes[i-1])+left_count
            if boxes[i-1]=="1":
                left_count += 1
        
        right_count = 0
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1]+int(boxes[i+1])+right_count
            if boxes[i+1]=="1":
                right_count+=1
        return [i+j for i,j in zip(pref, suff)]
