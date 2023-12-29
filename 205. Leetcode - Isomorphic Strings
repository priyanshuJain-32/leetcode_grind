class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_map = {}
        for i,j in zip(s,t):
            if (i not in st_map.keys()):
                if (j not in st_map.values()):
                    st_map[i]=j
                else:
                    return False
            elif i in st_map.keys() and st_map[i]!=j:
                return False
        return True
