class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        temp_count = 0
        while temp_count<len(students) and students:
            if students[0]==sandwiches[0]:
                temp_count = 0
                students.popleft()
                sandwiches.pop(0)
            else:
                temp_count += 1
                students.append(students.popleft())
        return len(students)