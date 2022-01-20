n = int(input())
stack = []
result = []
count = 0
possible = True
for _ in range(n):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break
if not possible:
    print("NO")
else:
    for i in result:
        print(i)