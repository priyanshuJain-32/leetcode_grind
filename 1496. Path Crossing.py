class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start = [0,0]
        seen = {(0,0)}
        for m in path:
            if m=="N":
                start[1] += 1
            elif m=="S":
                start[1] -= 1
            elif m=="E":
                start[0] += 1
            else:
                start[0] -= 1
            if tuple(start) in seen:
                return True
            seen.add(tuple(start))
        return False