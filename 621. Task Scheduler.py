class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        d = defaultdict(int)
        for i in tasks:
            d[i] += 1
        free = sorted(d, key=d.get, reverse=True)
        
        ans = (d[free[0]]-1)*(n+1) + list(d.values()).count(d[free[0]])

        return max(ans, m)
	
	# 1000 ways of not making a bulb

        # for k in free:
        #     temp = [k]
        #     for i in range(d[k]):
        #         temp.
        # return 0
        # waiting = deque()
        # wait = n
        # execute = []
        # while i<=j:
        #     curr = free[i]
        #     if i==j:
        #         if curr in waiting:
        #             if d[curr]>0:
        #                 execute.append('idle')
        #                 d[curr]-=1
        #             else:
        #                 break
        #         else:
        #             if d[curr]>0:
        #                 execute.append(curr)
        #                 d[curr]-=1
        #     elif curr not in waiting:
        #         if d[curr]>0:
        #             waiting.append(curr)
        #             execute.append(curr)
        #             d[curr]-=1
        #         else:
        #             i+=1
        #             continue
        #     else:
        #         curr = free[j]
        #         if d[curr]>0:
        #             waiting.append(curr)
        #             execute.append(curr)
        #             d[curr]-=1
        #         else:
        #             j-=1
        #             continue
        #     wait-=1
        #     if wait<=-1:
        #         try:
        #             waiting.popleft()
        #         except:
        #             continue
        # print(execute)
        # return len(execute)






        # # waiting = deque()
        # # seen, total, perform = 0, m, []
        # # wait = n

        # # while seen<total:
        # #     try:
        # #         task = free[-1]
        # #         if d[task]>0:
        # #             perform.append(task)
        # #             d[task]-=1
        # #             seen += 1
                    
        # #             waiting.append(task)
        # #     except:
        # #         perform.append("idle")
        # #         # perform +=1
            
        # #     wait-=1
        # #     if wait<=-1:
        # #         waiting.popleft()
            
        # # print(perform)
        # # return len(perform)