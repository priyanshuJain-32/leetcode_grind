class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        start, end = 10**5, 0

        if not intervals:
            return [newInterval]
            
        for i in intervals:
            if i[-1]>=newInterval[0]>=i[0] or i[-1]>=newInterval[-1]>=i[0]:
                start = min(start, i[0], newInterval[0])
                end = max(i[-1], newInterval[-1])
                continue
            
            if i[-1]<newInterval[0] or i[0]>newInterval[-1]:
                ret.append(i)
                continue
            
        if start==10**5 and end==0:
            ret.append(newInterval)
        else:
            ret.append([start,end])
        
        ret.sort(key=lambda x: x[0])
        return ret
