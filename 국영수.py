import sys
n = int(input())
students = []
for _ in range(n):
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    students.append([name, int(kor), int(eng), int(math)])

students.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(students[i][0])