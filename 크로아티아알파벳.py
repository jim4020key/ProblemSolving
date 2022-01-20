import sys
s = sys.stdin.readline().rstrip()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in alphabet:
    s = s.replace(i, "*")

print(len(s))