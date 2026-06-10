n = int(input())
s = list(map(int, input().split()))
j = [x for x in s if x % 2 != 0]
print(j)