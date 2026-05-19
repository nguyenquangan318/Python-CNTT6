import random

name_patient = input('Tên bệnh nhân: ')
gender = input('Giới tính: ')
birth_year = int(input('Năm sinh: '))
phone_number = input('Số điện thoại: ')
email = input('Email: ')
initial_symptoms = input('Triệu chứng ban đầu: ')
medical_fee = float(input('Chi phí khám: '))


id_patient ="BN" + str(birth_year) + str(random.randint(100, 999))


print('--- THẺ BỆNH NHÂN---')
print(f"Mã BN: {id_patient}")
print(f"Tên: {name_patient}")
print(f"Năm sinh: {birth_year}")
print(f"Điện thoại: {phone_number}")
print(f"Email: {initial_symptoms}")
print(f"Chi phí:{medical_fee} ")