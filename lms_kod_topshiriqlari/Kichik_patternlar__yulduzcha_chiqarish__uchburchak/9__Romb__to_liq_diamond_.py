a = int(input())
for i in range(1, a + 1):
    b = a - i
    c = 2 * i - 1
    print(' ' * b + '*' * c)
    
for i in range(a - 1, 0, -1):
    b = a - i
    c = 2 * i - 1
    print(' ' * b + '*' * c)