ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()
al = ids - banned
if not al:
    print("BO'SH")
else:
    print(*sorted(al))