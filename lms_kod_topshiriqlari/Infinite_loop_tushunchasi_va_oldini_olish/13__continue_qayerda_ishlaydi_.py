n = int(input())
skip = int(input())
for i in range(1, n + 1):
    if i == skip:
        continue
    print(i)