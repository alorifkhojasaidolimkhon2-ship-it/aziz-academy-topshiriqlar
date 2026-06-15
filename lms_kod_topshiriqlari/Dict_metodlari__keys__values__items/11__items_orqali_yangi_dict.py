n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
ne = {k: v * 2 for k, v in d.items()}
print(ne)