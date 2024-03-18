class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        prev = points[0][1]
        count = 1
        for s,e in points[1:]:
            if prev<s:
                count += 1
                prev = s
        return count
                
        # # n = len(points)
        # # if n==1:
        # #     return 1
        # # points.sort(key = lambda x: x[0])
        # # first = points[0]
        # # prev = set(range(first[0],first[1]+1))
        # # count = 0
        # # for i in range(1,n):
        # #     curr = set(range(points[i][0],points[i][1]+1))
        # #     intersect = prev.intersection(curr)
        # #     print(intersect)
        # #     if not intersect:
        # #         count += 1
        # #         prev = curr
        # #     else:
        # #         # count += 1
        # #         prev = intersect
        # # return count+1

        # def merge(points, n):        
        #     merged = []
        #     # seen = set()
        #     # n = len(points)
        #     prev = points[0]
        #     i = 1
        #     flag = False
        #     while i<n:
        #         curr = points[i]
        #         # if i==n-1:
        #         #     merged.append(curr)
        #         #     break
        #         # print(curr,prev)
        #         # if not prev:
        #         #     prev = curr
        #         #     i+=1
        #         #     continue
        #         if prev[1]<curr[0]:
        #             if not flag:
        #                 # if (prev[0],prev[1]) not in seen:
        #                 merged.append(prev)
        #                     # seen.add((prev[0],prev[1]))
        #             if i==n-1:
        #                 # if (curr[0],curr[1]) not in seen:
        #                 merged.append(curr)
        #                     # seen.add((curr[0],curr[1]))
        #                 break
        #             prev = curr
        #             flag = False
        #             i+=1
        #         else:
        #             temp_s, temp_e = max(curr[0],prev[0]), min(curr[1],prev[1])
        #             # if (temp_s, temp_e) not in seen:
        #             merged.append([temp_s, temp_e])
        #                 # seen.add((temp_s,temp_e))
        #             prev = [temp_s, temp_e]
        #             flag = True
        #             i+=1
            
        #     return merged, len(merged)
        # n = len(points)
        # if n==1:
        #     return 1
        # points.sort(key=lambda x: x[0])
        # # print(points)
        # for _ in range(n//2+1):
        #     points, l = merge(points, n)
        #     # print(points)
        #     if l==n or l==1:
        #         break
        #     n = l
        # # print(points)
        # return l