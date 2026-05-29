a, b = input().split()
b = int(b)
if a == 'admin':
    if b >= 18:
        print('Full access')
    else:
        print('Limited')
else:
    print('No access')