while True:
    a = int(input())
    if a == 0:
        print('Exit')
        break
    if a == 3:
        print('Correct')
        break
    elif a < 3:
        print('Low')
    else:
        print('High')