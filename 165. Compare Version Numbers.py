class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        i = 0
        m,n = len(v1),len(v2)
        flag = False
        if m>n:
            dim = n
            flag = True
        else:
            dim = m
        while i<dim:
            if v1[i]<v2[i]: return -1
            elif v1[i]>v2[i]: return 1
            i += 1
        if flag:
            if sum(v1[i:])>0:
                return 1
        else:
            if sum(v2[i:])>0:
                return -1
        return 0