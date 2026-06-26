s = 6
while True:
    a = int(input())
    if a < 1 or a > 10:
        print('Invalid')
        continue
    if a == 6:
        print('Correct')
        break