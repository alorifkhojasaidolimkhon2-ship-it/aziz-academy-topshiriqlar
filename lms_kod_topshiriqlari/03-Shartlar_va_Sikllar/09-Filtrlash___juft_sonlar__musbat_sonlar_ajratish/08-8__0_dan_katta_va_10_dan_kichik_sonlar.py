a = int(input())
b = list(map(int, input().split()))
for i in b:
    if 0 < i < 10:
        print(i)