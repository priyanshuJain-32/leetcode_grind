class Solution:
    def captureForts(self, forts: List[int]) -> int:
        i,j=0,0
        cnt = 0
        n = len(forts)
        d = {
            "start1":0,
            "start-1":0,
            "-1-1":0,
            "1-1":0,
            "-11":0,
            "11":0}
        s = "start"
        while i<n:
            if forts[i]==0:
                cnt += 1
            else:
                idx = s+str(forts[i])
                d[idx] = max(cnt,d[idx])
                cnt = 0
                s=str(forts[i])
            i+=1
        
        return max(d["-11"],d["1-1"])
