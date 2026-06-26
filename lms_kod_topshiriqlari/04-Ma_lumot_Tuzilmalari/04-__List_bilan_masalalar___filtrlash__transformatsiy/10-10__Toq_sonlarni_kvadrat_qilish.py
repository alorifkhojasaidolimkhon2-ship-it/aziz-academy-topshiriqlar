n = int(input())
s = list(map(int, input().split()))
r = [x**2 for x in s if x % 2 != 0]
print(r)