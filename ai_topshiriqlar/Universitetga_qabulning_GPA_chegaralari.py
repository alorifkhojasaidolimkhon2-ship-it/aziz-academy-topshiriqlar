# Universitetga qabulning GPA chegaralari
# Kurs: IT Dasturlash
# Mavzu: Solishtirish operatorlari: ==, !=, >, <, >=, <=
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
name, gpa = input().split()
gpa = float(gpa)
if 2.0 <= gpa <= 3.5:
    print('Qabul qilindi')
else:
    print('Qabul qilinmadi')