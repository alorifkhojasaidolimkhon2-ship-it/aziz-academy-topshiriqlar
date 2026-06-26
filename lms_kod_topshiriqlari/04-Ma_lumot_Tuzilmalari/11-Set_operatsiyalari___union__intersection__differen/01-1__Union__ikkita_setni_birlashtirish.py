a = set(map(int, input().split()))
b = set(map(int, input().split()))
n = sorted(a | b)
print(*n)
