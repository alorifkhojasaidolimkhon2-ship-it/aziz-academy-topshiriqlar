a, b = input().split()
b = int(b)
if a == 'admin':
    if b == 1:
        print('Admin active')
    else:
        print('Admin inactive')
else:
    print('User')