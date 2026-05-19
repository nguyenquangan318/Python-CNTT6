# first_num = int(input('Nhập số thứ 1: '))
# second_num = int(input('Nhập số thứ 2: '))

# Nếu số thứ 1 > số thứ 2 thì in ra hiệu 2 số
# Nếu số thứ 1 < số thứ 2 thì in ra tổng 2 số
# Nếu 2 số bằng nhau thì in ra tích 2 số
# if first_num > second_num:
#     print(f'Hiệu 2 số: {first_num - second_num}')
# elif first_num < second_num:
#     print(f'Tổng 2 số: {first_num + second_num}')
# else:
#     print(f'Tích 2 số: {first_num * second_num}')


# Nếu số thứ 1 = 1, in 'Xin chào'
# Nếu số thứ 1 = 2, in 'Tạm biệt'
# Nếu số thứ 1 = 0, in 'Thoát'
# Các trường hợp còn lại, in 'Lỗi'
# match first_num:
#     case 1:
#         print('Xin chào')
#     case 2:
#         print('Tạm biệt')
#     case 0:
#         print('Thoát')
#     case _:
#         print('Lỗi')


math_score = float(input('Nhập điểm toán'))
physic_score = float(input('Nhập điểm lý'))
lit_score = float(input('Nhập điểm văn'))
# Nếu chỉ 1 trong 3 điểm < 5, in "Thi lại"
# Nếu trên 2 điểm < 5, in "Học lại"
# Nếu cả 3 điểm > 5, in "Qua môn"

# Cách 1: Đếm số lượng điểm < 5
# In kết quả dựa trên số lượng đếm được
count_under_five = 0
if math_score < 5:
    count_under_five += 1
    
if physic_score < 5:
    count_under_five += 1
    
if lit_score < 5:
    count_under_five += 1
    
if count_under_five == 1:
    print('Thi lại')
elif count_under_five >= 2:
    print('Học lại')
else:
    print('Qua môn')