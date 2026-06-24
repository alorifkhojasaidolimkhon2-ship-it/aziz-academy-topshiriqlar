A = set(input().strip().split())
B = set(input().strip().split())
co = A & B
print(len(co))
for name in sorted(co):
    print(name)