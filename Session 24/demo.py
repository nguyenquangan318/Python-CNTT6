class Student:
    age = 18
    def __init__(self, id, name, phone = "Không có"):
        self.id = id
        self.name = name
        self.__phone = phone
        
    def say_hello(self):
        print(f'Xin chào, tôi tên là {self.name}')
    
    @staticmethod
    def check_phone(phone):
        if len(phone) < 10:
            print('Số điện thoại không hợp lệ')
            return False
        return True

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone
    
# student1 = Student(1, "Nguyễn Văn A", '0123456789')
# student2 = Student(2, "Nguyễn Thị B")
# print(student1.name)
# print(student2.phone)
# student1.say_hello()

# phone = input('Nhập số điện thoại sinh viên')
# if Student.check_phone(phone):
#     new_student = Student(1, "Nguyễn Văn C", phone)
#     print(Student.age)

student1 = Student(1, "Nguyễn Văn A", '0123456789')
# print(student1.get_phone())
print(student1.phone)
student1.phone = '0987654321'
print(student1.phone)
# student1.__phone = '09876543231'