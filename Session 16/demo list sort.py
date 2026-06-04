grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"stt": 3, "id": "SV02", "name": "Trần Thị C", "info": (8.0, 9.0)},
    {"stt": 4, "id": "SV02", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]

def print_student():
    print('--- DANH SÁCH SINH VIÊN')
    for student in grade_book:
        print('{id:<7} | {name:<20} | {info[0]:<10} | {info[1]:<10}'.format_map(student))
# names = [s['name'] for s in grade_book]
# names.sort()
# print(names)

# Sắp xếp toàn bộ sinh viên theo tên
grade_book.sort(key = lambda student: student['name'], reverse=True)
# Sắp xếp toàn bộ sinh viên theo điểm trung bình tăng dần
grade_book.sort(key = lambda student: student['info'][0] + student['info'][1])
student_sort = sorted(grade_book, key = lambda student: student['info'][0] + student['info'][1])
print_student()