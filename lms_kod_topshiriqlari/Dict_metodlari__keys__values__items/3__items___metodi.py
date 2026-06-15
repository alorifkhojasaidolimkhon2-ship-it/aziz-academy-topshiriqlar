n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
lst = list(d.items())
print(lst)