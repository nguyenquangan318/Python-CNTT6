# Lần lặp thứ 1
# Lần lặp thứ 2
# Lần lặp thứ 3
# Lần lặp thứ 4
# Lần lặp thứ 5
# Dừng lại ở lần lặp đầu tiên là số chẵn
# for i in range(1, 6):
#     if(i % 2 == 0):
#         break
#     print(f'Lần lặp thứ {i}')
    
# Chỉ in những lần lặp là số lẻ
for i in range(1, 6):
    if(i % 2 == 1):
        continue
    print(f'Lần lặp thứ {i}')
