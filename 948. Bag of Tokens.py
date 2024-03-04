class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i = 0
        j = len(tokens)-1
        score = 0
        tokens.sort()
        while i<=j:
            if i==j:
                if power>=tokens[i]:
                    score += 1
                    break
                else:
                    break
            if power>=tokens[i]:
                power-=tokens[i]
                score += 1
                i+=1
            elif power<tokens[i]:
                if score>0:
                    score-=1
                    power += tokens[j]
                j-=1
        return score