n = int(input())
s = list(map(int, input().split()))
m = [x for x in s if x < 0]
print(m)