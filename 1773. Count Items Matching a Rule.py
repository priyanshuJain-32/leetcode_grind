class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {
            "type":0,
            "color":1,
            "name":2
            }
        cnt = 0
        for i in items:
            idx = d[ruleKey]
            if i[idx]==ruleValue:
                cnt+=1
        return cnt