def divide(number):
    return 10/number

try:
    # code được kiểm tra
    number = float(input('Nhập số: '))
    result = divide(number)
except ValueError:
    # code khi try bị lỗi
    print('Lỗi giá trị không hợp lệ')
except ZeroDivisionError:
    print('Lỗi chia cho 0')
except:
    print('Lỗi không xác định')
else:
    print(f'Kết quả là: {result}')