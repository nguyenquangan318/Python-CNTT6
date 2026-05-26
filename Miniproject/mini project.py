qty_laptop = 0
qty_phone = 0
qty_tablet = 0
while True:
    print("""1.Xem báo cáo tồn kho
    2. Nhập kho
    3. Xuất kho
    4. Cảnh báo hàng tồn kho thấp
    5. Thoát chương trình.""")
    choice = int(input('Nhập lựa chọn: '))
    match choice:
        case 1:
            print(f'Laptop: {qty_laptop}')
            print(f'Phone: {qty_phone}')
            print(f'Tablet: {qty_tablet}')
        case 2:
            while True:
                print('1-Laptop\n2-Phone\n3-Tablet')
                product_choice = int(input('Chọn sản phẩm nhập: '))
                if(product_choice != 1 and product_choice != 2 and product_choice != 3):
                    print('Sản phẩm không hợp lệ')
                    continue
                quantity = int(input('Nhập số lượng sản phẩm: '))
                if(product_choice == 1):
                    qty_laptop += quantity
                elif(product_choice == 2):
                    qty_phone += quantity
                else:
                    qty_tablet += quantity
        # case 3:
        # case 4:
        case 5:
            print('Thoát chương trình')
            break
        case _:
            print('Thông tin không hợp lệ')