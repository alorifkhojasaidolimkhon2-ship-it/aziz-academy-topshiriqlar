count = 0
while True:
    a = int(input())
    count += 1
    if a == 1:
        print('Correct')
        break
    else:
        print('Try again')
print(count)