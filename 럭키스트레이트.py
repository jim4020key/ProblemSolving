n = input()
left = n[:len(n)//2]
right = n[len(n)//2:]

left = '+'.join(left)
right = '+'.join(right)
if eval(left) == eval(right):
    print("LUCKY")
else:
    print("READY")