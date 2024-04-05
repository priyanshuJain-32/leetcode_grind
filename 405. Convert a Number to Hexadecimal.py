class Solution:
    def toHex(self, num: int) -> str:
        def convert(b):
            b = (32-len(b))*"0"+b
            i = len(b)
            ans = ""
            while i>3:
                ans += d[int(b[i-4:i],2)]
                i-=4
            return ans[::-1]
        d = {
            0:"0",
            1:"1",
            2:"2",
            3:"3",
            4:"4",
            5:"5",
            6:"6",
            7:"7",
            8:"8",
            9:"9",
            10:"a",
            11:"b",
            12:"c",
            13:"d",
            14:"e",
            15:"f"}
        # if num==0:
        #     return "0"
        if num<0:
            num*=-1
            b = bin(num)[2:]
            b = (32-len(b))*"0"+b
            rev = ""
            for c in b:
                if c=="0":
                    rev += "1"
                else:
                    rev += "0"
            b = bin(int(rev,2)+1)[2:]
        else:
            b = bin(num)[2:]
        ans = convert(b)
        i = 0
        while i<len(ans)-1 and ans[i]=="0":
            i+=1
        return ans[i:]