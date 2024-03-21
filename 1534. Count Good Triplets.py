class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        dic1 = defaultdict(list)
        dic2 = defaultdict(list)
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                d = arr[i]-arr[j]
                if abs(d)<=a:
                    dic1[j].append(d)
        
        for j in range(1,n-1):
            for k in range(j+1, n):
                d = arr[j]-arr[k]
                if abs(d)<=b:
                    dic2[j].append(d)
                    
        for k,v in dic1.items():
            for i in v:
                for j in dic2[k]:
                    if abs(i+j)<=c:
                        cnt += 1
        return cnt