n = int(input())
nums = list(map(int, input().split()))
lst = []
for x in nums:
    lst.insert(0, x)
print(lst)