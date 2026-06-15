from tabulate import tabulate

def display_records(atendances):
    table = [["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"]]
    for atend in atendances:
        id = atend['id']
        name = atend['name']
        time_in = atend['times'][0]
        time_out = atend['times'][1] if atend['times'][1] else '[Đang làm việc]'
        table.append([id, name, time_in, time_out])
    print('--- BẢNG CHẤM CÔNG ---')
    print(tabulate(table, headers="firstrow", tablefmt="github"))