s = 8
u = False
for _ in range(3):
    a = int(input())
    if a == s:
        u = True
        break
if u:
    print('Correct')
else:
    print('Game Over')        