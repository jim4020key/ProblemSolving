n = int(input())
for _ in range(n):
    stack = []
    array = input()
    for i in array:
        if i == '(':
            stack.append(i)
        else:
            if stack and i == ')':
                if stack[-1] == '(':
                    stack.pop()
            else:  # 시작이 잘못된 케이스
                stack.append('/')

    if len(stack) == 0: print("YES")
    else: print("NO")