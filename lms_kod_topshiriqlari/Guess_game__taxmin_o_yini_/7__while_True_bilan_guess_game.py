s = 9
while True:
    a = int(input())
    if a == 9:
        print('Correct')
        break
    elif a < 9:
        print('Low')
    else:
        print('High')