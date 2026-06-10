n = int(input())
s = list(map(int, input().split()))
k = [abs(x) for x in s]
print(k)