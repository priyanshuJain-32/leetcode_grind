class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        target = len(rooms)
        open = set()
        open.add(0)
        count = 0
        while open:
            node = open.pop()
            seen.add(node)
            count += 1
            for r in rooms[node]:
                if r not in seen:
                    open.add(r)
        return count==target