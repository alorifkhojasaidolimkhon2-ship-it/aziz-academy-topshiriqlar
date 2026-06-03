lst = []
while True:
    s = input().split()
    if s[0] == 'stop':
        break
    if s[0] == 'append':
        lst.append(int(s[1]))
    elif s[0] == 'insert':
        lst.insert(int(s[1]), int(s[2]))
    elif s[0] == 'remove':
        x = int(s[1])
        if x in lst:
            lst.remove(x)
    elif s[0] == 'pop':
        lst.pop(int(s[1]))
print(lst)