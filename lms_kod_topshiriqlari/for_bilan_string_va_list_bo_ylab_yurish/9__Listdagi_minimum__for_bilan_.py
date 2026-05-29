n = int(input())
a = list(map(int, input().split()))
mn = a[0]
for x in a:
    if x < mn:
        mn = x
print(mn)