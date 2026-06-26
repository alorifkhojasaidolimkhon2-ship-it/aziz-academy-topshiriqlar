a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = b - a
if not c:
    print("BO'SH")
else:
    print(*sorted(c))