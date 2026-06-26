a = int(input())
sonlar = list(map(int, input().split()))
for son in sonlar:
    if son < 0:
       print(son)