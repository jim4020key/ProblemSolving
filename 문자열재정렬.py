s = input()
alphabet = []
result = 0

for x in s:
    if x.isalpha():
        alphabet.append(x)
    else: result += int(x)

alphabet.sort()
result_alpha = ''.join(alphabet)
print(result_alpha, end='')
if result != 0: print(result)