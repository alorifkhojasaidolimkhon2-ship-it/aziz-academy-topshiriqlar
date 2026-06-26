a = int(input())
b = list(map(int, input().split()))
c = 0
for i in b:
    if i % 5 == 0: 
        print(i)