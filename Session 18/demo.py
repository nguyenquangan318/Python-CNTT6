student_list = [{
    "id":"SV001",
    "full_name":"Nguyen Van A",
    "math": 8.5,
    "physics": 7.0,
    "chemis": 9.0,
    "avg": 8.17,
    "rank": "Giỏi"
}]

def display_students():
    for s in student_list:
        print(f'{s['id']:<7} | {s['full_name']:<20} | {s['math']:<10} | {s['physics']:<10} | {s['chemis']:<10} | {s['avg']:<10} | {s['rank']}')

def ranking(avg):
    if avg < 5:
        return 'Yếu'
    elif avg < 7:
        return 'TB'
    elif avg < 8:
        return 'Khá'
    else:
        return 'Giỏi'

def add_student():
    id = input('Nhập id sinh viên')
    full_name = input('Nhập tên sinh viên')
    math = float(input('Nhập điểm toán sinh viên'))
    physics = float(input('Nhập điểm lý sinh viên'))
    chemis = float(input('Nhập điểm hóa sinh viên'))
    avg = (math + physics + chemis) / 3
    rank = ranking(avg)
    student_list.append({
        "id": id,
        "full_name": full_name,
        "math": math,
        "physics": physics,
        "chemis": chemis,
        "avg": avg,
        "rank": rank
    })
    
def analyze_score():
    great_count = 0
    good_count = 0
    avg_count = 0
    weak_count = 0
    for s in student_list:
        if s['rank'] == 'Giỏi':
            great_count += 1
        elif s["rank"] == 'Khá':
            good_count += 1
        elif s["rank"] == 'TB':
            avg_count += 1
        else:
            weak_count += 1
    print(f'Giỏi: {great_count} sinh viên')
    print(f'Khá: {good_count} sinh viên')
    print(f'Trung bình: {avg_count} sinh viên')
    print(f'Yếu: {weak_count} sinh viên')

while True:
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach")
    print("2. Them sinh vien")
    print("3. Cap nhat sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien theo ma")
    print('6. Tim kiem sinh vien theo ten')
    print("7. Thong ke hoc luc")
    print("8. Thoat")
    choice = input("Nhap lua chon: ")
    match choice:
        case '1':
            display_students()
        case '6':
            analyze_score()
        case '7':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')