s = 20
c = 0
while True:
    a = int(input())
    c += 1
    if a == s:
        print('Correct')
        print(c)
        break
    elif a < s:
        print('Low')
    else:
        print('Invalid')