n = int(input())
lst = list(map(int, input().split()))
x = int(input())
while x in lst:
    lst.remove(x)
print(lst)