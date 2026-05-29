n, m = map(int, input().split())
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * m)
    else:
        print('*' + '.' * (m - 2) + '*')