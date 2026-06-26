a = input().split()
mx = a[0]
for w in a:
    if len(w) > len(mx):
        mx = w
print(mx)