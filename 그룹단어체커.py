n = int(input())
count = 0
for _ in range(n):
    word = input()
    group_word = True
    prev = ['']
    for i in word:
        if i != prev[-1] and i in prev:
            group_word = False
            break
        else:
            prev.append(i)
    if group_word:
        count += 1

print(count)
