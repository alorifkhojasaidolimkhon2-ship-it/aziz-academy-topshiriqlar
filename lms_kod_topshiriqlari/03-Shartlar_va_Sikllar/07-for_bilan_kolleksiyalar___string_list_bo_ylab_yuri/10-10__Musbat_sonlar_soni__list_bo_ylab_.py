n = int(input())
a = list(map(int, input().split()))
b = 0
for x  in a:
    if x > 0:
        b += 1
print(b)