class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        
        for e in emails:
            for c in e:
                if c=="@":
                    break
                elif c=="+":
                    e = e.split("+")
                    e = e[0]+"@"+e[-1].split("@")[-1]
                    break
                elif c==".":
                    e = e.replace(".","",1)
                       
            unique.add(e)
        
        return len(unique)