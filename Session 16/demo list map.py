grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"stt": 3, "id": "SV02", "name": "Trần Thị C", "info": (8.0, 9.0)},
    {"stt": 4, "id": "SV02", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]

# Lấy ra danh sách chỉ chứa tên sinh viên
# ["Nguyễn Văn A", "Trần Thị B", "Trần Thị C", "Nguyễn Văn D"]

# Dùng vòng lặp for
student_names = []
for student in grade_book:
    student_names.append(student['name'])
print(student_names)

# Dùng hàm map
# Dùng hàm thường
def get_name(student):
    return student['name']
student_names = list(map(get_name, grade_book))
print(student_names)

# Dùng hàm lambda
student_names = list(map(lambda student: student['name'], grade_book))
print(student_names)

# Dùng list comprehension
student_names = [student['name'] for student in grade_book]
print(student_names)

# Lấy ra danh sách chỉ chứa tên sinh viên, tất cả tên được viết thường
normal_names = [student['name'].lower() for student in grade_book]
print(normal_names)

# Lấy ra danh sách chỉ chứa tên, không chứa họ và tên đệm
names_only = [s['name'].split()[-1] for s in grade_book]
print(names_only)