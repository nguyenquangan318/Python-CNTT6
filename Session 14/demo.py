grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

good_grade = [
    {"id": "SV03", "name": "Nguyễn Văn C", "info": (10, 9.0)},
    {"id": "SV04", "name": "Trần Thị D", "info": (9.5, 9.0)}
]
teacher = 'Nguyen Quang An'
def print_student(students = grade_book):
    for student in students:
        print(student)
        print(f'Điểm trung bình là: {avg_score(student)}')
        print(f'Giảng viên là: {teacher}')
        
def avg_score(student):
    '''Hàm tính điểm trung bình của sinh viên

    Args:
        student (dictionary): cấu trúc sinh viên

    Returns:
        float: Điểm trung bình tính được
    '''
    first_score, second_score = student['info']
    avg = (first_score + second_score) / 2
    return avg
        
print_student()
print_student(good_grade)