class Solution:
    def __init__(self):
        self.d = defaultdict(int)
    def numSquares(self, n: int) -> int:
        def solve(n):
            if n==0:
                return 0
            if n<0:
                return float('inf')
            if n in self.d:
                return self.d[n]
            mini = n
            i = 1
            while i*i<=n:
                mini = min(mini,solve(n-i*i))
                i+=1
            self.d[n] = mini+1
            return self.d[n]
        # self.d[n] = solve(n)
        solve(n)
        return self.d[n]

#         self.d = {0:0}
#         def helper(n):
#             if n<=0:
#                 return 0
#             for i in range(1,n+1):
#                 j = 1
#                 while j*j<=i:
#                     self.d[i] = min(self.d.get(i,100000),self.d[i-j*j]+1)
#                     j+=1
                    
#         helper(n)
#         return self.d[n]
        
#         # if n<4:
#         #     return n
#         # squares = []
#         # s = 1
#         # i = 1
#         # length = 0
#         # while s<=n:
#         #     squares.append(s)
#         #     length+=1
#         #     i += 1
#         #     s = i*i
#         # if squares[-1]==n:
#         #     return 1
#         # ans = 100000
#         # k = length-1
        
#         # # print(squares)
#         # while k>-1:
#         #     d = squares[k]
#         #     N = n
#         #     count = 0
#         #     L = []
#         #     c = 100000
#         #     while N>0:
#         #         L.append(d)
#         #         if N%d==0:
#         #             c = N//d
#         #             ans = min(ans,count+c)
#         #             # break
#         #         N -= d
#         #         idx,found = self.bsearch(squares,N,length)
#         #         # print(idx)
#         #         count += 1
#         #         # if found==1:
#         #         #     count += 1
#         #         #     break
#         #         # else:
#         #         #     count += 1
#         #         d = squares[idx]
#         #     ans = min(ans,count)
#         #     k-=1
#         #     print(L,count)
#         # return ans
    
#     def bsearch(self,L,v,length):
#         l = 0
#         r = length-1
#         while l<=r:
#             m = (l+r)//2
#             if L[m]==v:
#                 return m,1
#             elif L[m]>v:
#                 r = m-1
#             else:
#                 l = m+1
#         return l-1,0
    
            