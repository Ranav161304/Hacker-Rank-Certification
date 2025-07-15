from collections import namedtuple

n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)

total_marks = 0

for _ in range(n):
    data = input().split()
    student = Student(*data)
    total_marks += int(student.MARKS)

print(f"{total_marks / n:.2f}")
