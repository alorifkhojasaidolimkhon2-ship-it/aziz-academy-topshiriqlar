lst = [1, 2, 3]
x = int(input())
if x in lst:
    lst.remove(x)
    print('Removed')
else:
    print('Not found')
print(lst)