n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for k, v in d.items():
    if v > 50:
        print(v)