a = input().strip()
b = input().strip()
c = set(a) & set(b)
if not c:
    print("BO'SH")
else:
    print("".join(sorted(c)))