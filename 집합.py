# 시간초과대박
import sys
m = int(input())
data = set()

for _ in range(m):
    command = sys.stdin.readline().rstrip().split()
    if len(command) == 1:
        if command[0] == "all":
            data.clear()
            data = set([i for i in range(1, 21)])
        else:
            data = set()
        continue

    x = int(command[1])
    command = command[0]
    if command == "add":
        data.add(x)
    elif command == "remove":
        if x in data: data.remove(x)
    elif command == "check":
        print(1 if x in data else 0)
    elif command == "toggle":
        if x in data:
            data.remove(x)
        else:
            data.add(x)