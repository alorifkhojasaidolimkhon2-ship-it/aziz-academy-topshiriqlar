a, b = map(int, input().split())
c = input()
if c == 'add':
    print(a+b)
elif c == 'sub':
    print(a-b)
elif c == 'mul':
    print(a*b)
else:
    print(a/b)