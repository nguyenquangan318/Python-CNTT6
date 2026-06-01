students = ['Anh', 'Diệp', 'Lê', 'Trung']
# Thêm vào cuối
students.append('Long')
# Thêm vào vị trí
students.insert(0, 'Dũng')
# Nối danh sách
students.extend(['1','2','3'])
students += ['4', '5']

# Sửa phần tử trong danh sách
# Sửa sinh viên đầu tiên thành 'Đạt'
students[0] = 'Đạt'
# Sửa sinh viên cuối cùng thành 'Đạo
# students[-1] = 'Đạo'
students[len(students) - 1] = 'Đạo'
# Sửa sinh viên tên là 'Trung' thành 'An'
trung_index = students.index('Trung')
students[trung_index] = 'An'

# Xóa phần tử trong danh sách
# Xóa theo giá trị
students.remove('1')
# Xóa theo chỉ mục
students.pop(6)
# Xóa 1 phần danh sách
del students[6:8]

print(students)