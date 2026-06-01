# Duyệt danh sách
students = ['Anh', 'Diệp', 'Lê', 'Trung']
    
for student in students:
    print(student)
# 1. Anh
# 2. Diệp
# ...
for i, student in enumerate(students):
    print(f'{i+1}. {student}')