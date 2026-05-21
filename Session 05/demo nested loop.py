# for i in range(5):
#     print(f'Vòng lặp bên ngoài lần {i}')
#     for j in range(3):
#         print(f'Vòng lặp bên trong lần {j}')
#     print()
    
user_input = int(input('Nhập số nguyên dương bất kỳ: '))
# In ra số dấu * trên 1 dòng là số đã nhập
for i in range(user_input):
    print('*', end='')