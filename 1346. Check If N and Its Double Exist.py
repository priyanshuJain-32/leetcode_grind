class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if n*2 in seen or n/2 in seen:
                return True
            seen.add(n)
        return False
        
        # def bsearch(arr,k,n):
        #     l = 0
        #     r = n-1
        #     while l<=r:
        #         m = (l+r)//2
        #         if arr[m]==k:
        #             return True
        #         elif arr[m]>k:
        #             r = m-1
        #         else:
        #             l = m+1
        #     return False
        # arr.sort()
        # n = len(arr)
        # for i in range(n-1):
        #     if arr[i]<0:
        #         to_search = arr[i]/2
        #     else:
        #         to_search = 2*arr[i]
        #     if bsearch(arr[i+1:],to_search,n-i-1):
        #         return True
        # return False
                
