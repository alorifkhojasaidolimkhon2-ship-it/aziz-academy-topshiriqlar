n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for val in d.values():
    print(val)