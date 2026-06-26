n = int(input())
lst = list(map(int, input().split()))
if len(lst) >= 5:
    print(lst[5])
else:
    print('Error')