# eval함수를 쓰려면 리스트 append ... 수식의 우선순위를 지키기가 ...
# 숫자가 두개 붙어 있으면 더하기
s = input()
stack = []

for i in s:
    if i in ['(', '[']:
        stack.append(i)
    else:
        if stack and i == ')':
            if len(stack) > 1 and str(stack[-1]).isdigit() and stack[-2] == '(':
                n = stack.pop()*2
                stack.pop()
                stack.append(n)
            elif stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:       # 쌍이 맞지 않는 케이스 ex) (()([())])
                stack.append('/')
                break

        elif stack and i == ']':
            if len(stack) > 1 and str(stack[-1]).isdigit() and stack[-2] == '[':
                n = stack.pop()*3
                stack.pop()
                stack.append(n)
            elif stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                stack.append('/')
                break
        else:       # 시작이 잘못된 케이스 ex) ]()
            stack.append('/')
            break
    if len(stack) > 1 and str(stack[-1]).isdigit() and str(stack[-2]).isdigit():
        stack.append(stack.pop()+stack.pop())
if len(stack) == 1 and str(stack[-1]).isdigit():
    print(stack.pop())
else:
    print(0)
