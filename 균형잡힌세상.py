import sys

while(True):
    stack = []
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        print("no" if stack else "yes")