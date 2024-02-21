class Solution:
    def average(self, salary: List[int]) -> float:
        maxi = 999
        mini = 1_000_001
        total = 0
        for i in salary:
            if i>maxi:
                maxi = i
            if i<mini:
                mini = i
            total += i
        return (total - maxi - mini)/(len(salary)-2)