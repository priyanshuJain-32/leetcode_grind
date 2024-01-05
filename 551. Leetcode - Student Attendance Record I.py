class Solution:
    def checkRecord(self, s: str) -> bool:
        # Noob
        absent = 0
        late = 0
        present = 0
        for i in s:
            if i=="A":
                absent += 1
                late = 0
                if absent >1:
                    return False
            elif i=="L":
                late += 1
                if late==3:
                    return False
            else:
                late = 0
        return True

        # Pro
        # return s.count("A")<2 and "LLL" not in s
