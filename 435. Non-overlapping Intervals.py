class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        p = intervals[0][1]
        c = 0
        for i in range(1,len(intervals)):
            s = intervals[i][0]
            if p<=s:
                p = intervals[i][1]
            else:
                c+=1
        return c