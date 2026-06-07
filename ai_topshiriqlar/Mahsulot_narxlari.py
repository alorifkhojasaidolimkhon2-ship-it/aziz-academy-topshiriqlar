# Mahsulot narxlari
# Kurs: IT Dasturlash
# Mavzu: 2-mavzu: Birinchi dastur, print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

a, b = input().split()
n = int(input())
c, d = input().split()
y = int(input())
found = False
if n == 1:
    print(a, b)
    found = True
if y == 1:
    print(c, d)
    found = True
if not found:
    print('Hech qanday mahsulot chiptalanmagan')