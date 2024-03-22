class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        m = len(flowerbed)
        # Handle edge cases for m==1
        if m==1:
            if n==1 and flowerbed[0]==0:
                return True
            elif n==0 and flowerbed[0]==1:
                return True
            elif n==0 and flowerbed[0]==0:
                return True
            else:
                return False
        if m<=n:
            return False
        elif m<3:
            return not (sum(flowerbed)==1) or n==0

        i = 1
        # Handle first
        if flowerbed[0]==0 and flowerbed[1]==0 and n>0:
            flowerbed[0]=1
            n-=1
        # Handle last
        if flowerbed[-1]==0 and flowerbed[-2]==0 and n>0:
            flowerbed[-1] = 1
            n-=1
        # Handle middle
        while n>0 and i<m-1:
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            i+=1
        return n==0