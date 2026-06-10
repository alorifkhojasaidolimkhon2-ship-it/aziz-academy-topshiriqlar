n = int(input())
s = list(map(int, input().split()))
r = list(map(lambda x: x * 10, filter(lambda x: x % 2 == 0, s)))
print(r)