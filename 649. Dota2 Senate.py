class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        countR = countD = 0

        for s in senate:
            if s=='R':
                countR += 1
                continue
            countD += 1
        
        while countR and countD:
            if senate[0]=='R':
                senate = senate[1:].replace('D','',1)+senate[0]
                countD -= 1
            else:
                senate = senate[1:].replace('R','',1) + senate[0]
                countR -= 1

        if countR==0:
            return 'Dire'
        elif countD==0:
            return 'Radiant'