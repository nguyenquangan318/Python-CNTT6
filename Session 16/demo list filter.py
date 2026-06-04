grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"stt": 3, "id": "SV02", "name": "Trần Thị C", "info": (8.0, 9.0)},
    {"stt": 4, "id": "SV02", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]

# Lọc ra danh sách sinh viên có điểm trung bình > 8
# Dùng vòng lặp for
good_students = []
for student in grade_book:
    avg = (student['info'][0] + student['info'][1]) / 2
    if avg > 8:
        good_students.append(student['name'])
print(good_students )

# Dùng hàm filter
# Dùng hàm thường
def check_avg(student):
    avg = (student['info'][0] + student['info'][1]) / 2
    return avg > 8
good_students = list(filter(check_avg, grade_book))
print(good_students)

# Dùng hàm lambda
good_students = list(filter(lambda student: (student['info'][0] + student['info'][1]) / 2 > 8, grade_book))
print(good_students)

# Dùng list comprehension
good_students = [student for student in grade_book if (student['info'][0] + student['info'][1]) / 2 > 8]
print(good_students)

# Tính tổng điểm của toàn bộ sinh viên
total = sum([student['info'][0] + student['info'][1] for student in grade_book])
print(total)