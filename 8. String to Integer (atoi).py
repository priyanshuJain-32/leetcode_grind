class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        max_int = 2147483647
        min_int = -2147483648
        sign = 1
        if s=="":
            return 0
        elif s[0]=="-":
            sign = -1
            s=s[1:]
        elif s[0]=="+":
            sign = 1
            s=s[1:]
        elif not (s[0].isdigit() or s[0].isspace()):
            return 0
        elif s.isnumeric():
            return max(min_int, min(max_int, int(s)*sign))
        
        digit_flag = False
        num = ''
        for i in s:
            if i.isdigit():
                num+=i
                digit_flag = True
            elif i.isspace() and (digit_flag):
                break
            else:
                break
        try:
            return max(min_int, min(max_int, int(num)*sign))
        except:
            return 0
