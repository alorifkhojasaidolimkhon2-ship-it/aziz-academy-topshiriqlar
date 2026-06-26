a = int(input())
data = list(map(int, input().split()))
b = data[0]
for i in range(1, a):
    if data[i] > b:
        b = data[i]
print(b)