class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        starts = set()
        for s,e in paths:
            cities.add(s)
            cities.add(e)
            starts.add(s)
        return (cities-starts).pop()