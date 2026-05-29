a = int(input())
b = a % 4 == 0 and a % 100 !=0
c = a % 400 == 0
print(b or c)