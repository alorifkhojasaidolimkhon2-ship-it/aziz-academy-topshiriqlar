s = input().split()
if len(s) == 1:
    print(0)
else:
    a, b = map(int, s)
    if a == b:
        print(1)
    else:
        print(0)