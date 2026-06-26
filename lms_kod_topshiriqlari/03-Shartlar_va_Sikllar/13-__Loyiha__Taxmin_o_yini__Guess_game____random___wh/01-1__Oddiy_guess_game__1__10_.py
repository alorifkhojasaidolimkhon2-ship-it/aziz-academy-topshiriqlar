s = 7
while True:
    a = int(input())
    if a < s:
        print('Low')
    elif a > s:
        print('High')
    else:
        print('Correct')
        break