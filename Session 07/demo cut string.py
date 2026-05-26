date_of_birth = '25/05/2026'
# string_name[start:stop:step]

date = date_of_birth[0:2:1]
date = date_of_birth[:2]

month = date_of_birth[3:5:1]
month = date_of_birth[3:5]

year = date_of_birth[6:10:1]
year = date_of_birth[6:]
year = date_of_birth[-4:]

reverse = date_of_birth[::-1]

print(date)
print(month)
print(year)
print(reverse)

print('27' in date_of_birth)