raw_input = "   nGuyen vaN aN  ;  2004   "
while True:
    choice = input('''
===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
=====================================
Nhập lựa chọn của bạn (1-4): ''')
    match choice:
        case '1':
            print(f'Chuỗi dữ liệu gôc hiện tại:\n{raw_input}')
        case '2':
            input_list = raw_input.split(';')
            full_name = input_list[0]
            full_name = full_name.strip()
            full_name = full_name.title()
            birth_year = input_list[1]
            age = 2026 - int(birth_year)
            print(f'''
[KÊT QUẢ CHUẨN HÓA DỮ LIỆU]:
- Họ và tên: {full_name}
- Tuổi hiện tại: {age} tuổi''')
        # case '3':
    
        case '4':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')