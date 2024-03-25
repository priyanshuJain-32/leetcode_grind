class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        d = []
        l = []
        max_len = 0
        
        for num in nums:
            bit = bin(num)[2:]
            n = len(bit)
            d.append(bit)
            l.append(n)
            max_len = max(n, max_len)
        
        for i in range(len(d)):
            if l[i]<max_len:
                d[i] = "0"*(max_len-l[i]) + d[i]
        
        ans = ""
        for i in range(max_len):
            temp = ""
            for j in range(len(d)):
                temp += d[j][i]
            if temp.count("1")>=k:
                ans += "1"
            else:
                ans += "0"
        return int(ans,2)