class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        
        # Reverse approach
        for r in range(m-2,-1,-1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r+1][c],triangle[r+1][c+1])
        return triangle[0][0]

        # Straigt Approach
        # for r in range(m):
        #     n = len(triangle[r])
        #     for c in range(n):
        #         if r-1>-1:
        #             if c==n-1:
        #                 prev = triangle[r-1][c-1]
        #             elif c-1>-1:
        #                 prev = min(triangle[r-1][c-1],triangle[r-1][c])
        #             else:
        #                 prev = triangle[r-1][c]
        #         else:
        #             prev = 0
        #         triangle[r][c]+=prev
        # return min(triangle[-1])