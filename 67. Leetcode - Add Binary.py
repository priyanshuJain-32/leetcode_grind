class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = ''
        s = list(str(int(a)+int(b)))
        n = len(s)-1

        while n>0:
            if s[n]=='2':
                s[n]='0'
                s[n-1] = str(int(s[n-1])+1)
            elif s[n]=='3':
                s[n]='1'
                s[n-1] = str(int(s[n-1])+1)
            n-=1
        if s[0]=='2':
            s[0]='0'
            s = ['1'] + s
        elif s[0]=='3':
            s[0] = '1'
            s = ['1'] + s
        for i in s:
            ret += i
        return ret

        # Alternate
        # return str(bin(int(a,2)+int(b,2)))[2:]

