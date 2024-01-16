class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_home = {"M":0, "G":0, "P":0}
        pick_t = 0
        flag_M, flag_G, flag_P = False, False, False
        for i in range(len(garbage)-1, -1, -1):
            if "M" in garbage[i] and not flag_M:
                last_home["M"] = i
                flag_M = True
            if "G" in garbage[i] and not flag_G:
                last_home["G"] = i
                flag_G = True
            if "P" in garbage[i] and not flag_P:
                last_home["P"] = i
                flag_P = True
            pick_t+=len(garbage[i])
        for k,v in last_home.items():
            if v!=0:
                pick_t+=sum(travel[:v])
        return pick_t
