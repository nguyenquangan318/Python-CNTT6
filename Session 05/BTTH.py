# Nhập số lượng nhân viên

staff_number = int(input('Nhập số lượng nhân viên: '))
for i in range(staff_number):
    # Nhập thông tin cho từng nhân viên
    staff_name = input('Nhập tên nhân viên: ')
    work_days = int(input('Nhập số ngày làm: '))
    if(work_days < 0 or work_days > 22):
        print('Dữ liệu không hợp lệ')
        continue
    # In thông tin nhân viên vừa nhập theo yêu cầu
    print(f'{staff_name}: ', end = '')
    for j in range(work_days):
        print('*', end='')
    # Thống kê mức độ làm việc
    