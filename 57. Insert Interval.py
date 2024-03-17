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

# Improved
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        s, e = newInterval
        # flag = False
        # temp_s, temp_e = 100001, -1
        # if not intervals:
        #     return [newInterval]

        for i in range(len(intervals)):
            start,end = intervals[i]
            if e<start:
                ret.append([s,e])
                ret += intervals[i:]
                return ret
            elif s>end:
                ret.append(intervals[i])
            else:
                s, e = (min(s,start),max(e,end))
        ret.append([s,e])
            # if s<start:
            #     temp_s = min(temp_s,s, start)
            #     if start<=e<=end:
            #         temp_e = max(e,end,temp_e)
            #         ret.append([temp_s,temp_e])
            #         flag = True
            #         ret += intervals[i+1:]
            #         break
            #     elif e<start:
            #         ret.append([temp_s,e])
            #         flag = True
            #         ret.extend(intervals[i:])
            #         break
            #     elif e>end:
            #         if i==len(intervals)-1:
            #             ret.append([temp_s,e])
            #             flag = True
            #         continue

            # elif start<=s<=end:
            #     temp_s = min(s,start,temp_s)
            #     if start<=e<=end:
            #         temp_e = max(e,end,temp_e)
            #         ret.append([temp_s,temp_e])
            #         flag = True
            #         ret += intervals[i+1:]
            #         break
            #     elif e>end:
            #         if i==len(intervals)-1:
            #             ret.append([temp_s,e])
            #             flag = True
            #         continue
            # elif s>end and e>end:
            #     ret.append([start,end])
        

        # if not flag: ret.append([s,e])    
        return ret