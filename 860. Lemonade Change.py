class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        D = {5:0,10:0,20:0}
        for i in bills:
            D[i]+=1
            if i==20:
                if D[10]>0:
                    D[10] -= 1
                    if D[5]>0:
                        D[5] -= 1
                    else:
                        return False
                elif D[5]>2:
                    D[5] -= 3
                else:
                    return False
            elif i==10:
                if D[5]>0:
                    D[5]-=1
                else:
                    return False
        return True