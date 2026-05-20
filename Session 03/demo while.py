# user_input = input("Nhập số bất kỳ")
# Cho người dùng nhập đến bao giờ người dùng nhập 0 thì dừng
# Nếu nhập số khác thì in 'Chưa đúng'
# while user_input != 0:
#     print('Chưa đúng')
#     user_input = input("Nhập số bất kỳ")
    
# In và thực hiện chức năng
# ---MENU---
# 1. Nhập tên
# Cho người dùng nhập tên và in 'Xin chào ...'
# 2. Xóa tên
# In 'tạm biệt ...', đặt tên thành chuỗi rỗng
# 3. Thoát
# In 'Thoát chương trình'
choice = 1
user_name = ""
while choice != 3:
    print('---MENU---')
    print('1. Nhập tên')
    print('2. Xóa tên')
    print('3. Thoát')
    choice = int(input('Lựa chọn của bạn là: '))
    match choice:
        case 1:
            user_name = input('Nhập tên: ')
            print(f'Xin chào {user_name}')
        case 2:
            print(f'Tạm biệt {user_name}')
            user_name = ""
        case 3:
            print('Thoát chương trình')
        case _:
            print('Lựa chọn không hợp lệ')