grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades(book):
    print('--- BẢNG ĐIỂM HỌC SINH ---')
    print(f'{'Mã SV':<7} | {'Tên học sinh':<15} | {'Điểm toán':<10} | {'Điểm anh':<10} | ĐTB')
    print('-'*65)
    for student in book:
        math, eng = student['info']
        avg = (math + eng) / 2
        print(f'{student['id']:<7} | {student['name']:<15} | {math:<10} | {eng:<10} | {avg}')
    print('-'*65)
    
def add_student(book):
    while True:
        check = False
        input_id = input('Nhập mã sinh viên mới: ')
        for student in book:
            if student['id'] == input_id:
                check = True
                print('id đã tồn tại')
                break
        if not check:
            break   
    input_name = input('Nhập tên sinh viên mới: ')
    input_math = float(input('Nhập điểm toán: '))
    input_eng = float(input('Nhập điểm anh: '))
    new_student = {
        "stt": 1 if len(book) == 0 else book[len(book)-1]['stt'] + 1,
        "id": input_id,
        "name": input_name,
        "info": (input_math, input_eng)
    }
    book.append(new_student)
    
while True:
    choice = input('''=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
Chọn chức năng (1-5): ''')
    match choice:
        case '1':
            display_grades(grade_book)
        case '2':
            add_student(grade_book)
        case '5':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')