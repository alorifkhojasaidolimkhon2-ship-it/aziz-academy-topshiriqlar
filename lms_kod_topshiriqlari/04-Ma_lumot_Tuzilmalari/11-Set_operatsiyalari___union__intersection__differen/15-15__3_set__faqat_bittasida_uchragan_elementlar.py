A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
r = (A - B - C) | (B - A - C) | (C - A - B)
if not r:
    print("BO'SH")
else:
    print(*sorted(r))