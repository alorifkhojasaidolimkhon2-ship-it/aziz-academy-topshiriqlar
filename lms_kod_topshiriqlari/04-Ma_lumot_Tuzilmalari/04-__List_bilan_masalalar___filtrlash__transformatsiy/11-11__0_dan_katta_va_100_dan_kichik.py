n = int(input())
nums = list(map(int, input().split()))
res = [x for x in nums if 0 < x < 100]
print(res)