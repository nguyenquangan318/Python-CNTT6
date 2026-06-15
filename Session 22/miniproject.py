import logging
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def add_device(devices):
    while True:
        id = input('Nhập mã')
        # Kiểm tra mã bị trống
        if (id == ""):
            print('Mã không được trống')
            # Nếu mã trống thì chạy lại vòng lặp từ đầu
            continue
        # Kiểm tra mã bị trùng
        check = False
        for device in devices:
            if id == device['id']:
                check = True
                break
        if check:
            # Nếu mã trùng thì chạy lại vòng lặp từ đầu
            continue
        break
    
    location = input('Nhập địa điểm')
    while True:
        try :
            old_index = int(input('Nhập chỉ số cũ'))
        except:
            print('Lỗi')  
            continue
        else:
            if(old_index < 1000 or old_index > 3000):
                print('Vượt giới hạn')
                continue
            break
    new_index = input('Nhập chỉ số mới')
    status = input('Nhập trạng thái')
    devices.append({
        'id': id,
        'location': location,
        'old_index': old_index,
        'new_index': new_index,
        'status': status
    })

def main():

    devices_main = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
    ]
    

    while True:
        print('''
        ==== SMART ENERGY MONITOR - PHÒNG Cơ ĐIỆN =====
        1. Xem danh sách thiêt bị giám sát
        2. Thêm chỉ sô điện tiêu thụ (Check-in)
        3. Kích hoạt trạng thái cảnh báo quá tải
        4. Tính tổng lượng điện & Chi phí năng lượng
        5. Thoát chương trình
        ===============================================
        ''')
        try:
            choice = int(input("\nMời chọn chức năng (1-5): "))
        except ValueError:
            print("[Lỗi]: Vui lòng nhập số từ 1 đến 5!")
            continue
        match choice:
            # case 1:
            #     show_devices(devices_main)
            # case 2:
            #     update_indices(devices_main)
            # case 3:
            #     activate_overload_warning(devices_main)
            # case 4:
            #     show_financial_report(devices_main)
            case 5:
                print("\nCảm ơn bạn đã sử dụng Smart Energy Monitor!")
                print("[Chương trình kết thúc]")
                break
            case _:
                print("[Lỗi]: Vui lòng chọn từ 1 đến 5!")

if __name__ == "__main__":
    main()