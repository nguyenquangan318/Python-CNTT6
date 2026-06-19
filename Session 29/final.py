class Product:
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ""
    
    def calculate_revenue(self):
        self.total_revenue = self.price * self.quantity_sold - self.discount
    
    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"
    
class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self):
        id = input("Nhập mã sản phẩm: ")
        name = input("Nhập tên sản phẩm: ")

        while True:
            try:
                price = float(input("Nhập giá sản phẩm: "))
                break
            except:
                print("Giá nhập không hợp lệ, vui lòng nhập lại")
        
        quantity_sold = int(input("Nhập số lượng sản phẩm đã bán: "))
        discount = float(input("Nhập số tiền giảm cho sản phẩm: "))
        new_product = Product(id, name, price, quantity_sold, discount)
        new_product.calculate_revenue()
        new_product.classify_revenue()
        self.products.append(new_product)

    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm trống")
            return
        print("DANH SÁCH SẢN PHẨM")
        for p in self.products:
            print(f"{p.id:<7} | {p.name:<15} | {p.price:<10} | {p.quantity_sold:<5} | {p.discount:<10} | {p.total_revenue:<15} | {p.revenue_type}")

    def update_product(self):
        update_id = input("Nhập mã sản phẩm muốn sửa: ")
        for p in self.products:
            if p.id == update_id:
                # Cập nhật thông tin mới
                p.price = float(input("Nhập giá mới cho sản phẩm: "))
                p.quantity_sold = int(input("Nhập số lượng đã bán mới: "))
                p.discount = float(input("Nhập số tiền được giảm mới: "))
                p.calculate_revenue()
                p.classify_revenue()
                return
        print("Không tìm thấy sản phẩm")
            
    def delete_product(self):
        delete_id = input("Nhập mã sản phẩm muốn xóa: ")
        for p in self.products:
            if p.id == delete_id:
                # xóa sản phẩm
                confirm_del = input('Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ')
                if(confirm_del == "Y"):
                    self.products.remove(p)
                return
        print("Không tìm thấy sản phẩm")
        
    def search_product(self):
        search_name = input("Nhập tên sản phẩm muốn tìm")
        search_result = []
        for p in self.products:
            if search_name in p.name:
                search_result.append(p)
        if not search_result:
            print("Không tìm thấy")
        else:
            for p in search_result:
                print(f"{p.id:<7} | {p.name:<15} | {p.price:<10} | {p.quantity_sold:<5} | {p.discount:<10} | {p.total_revenue:<15} | {p.revenue_type}")

main = ProductManager()
while True:
    choice = input('''================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thống kê doanh thu
7. Thoát
=====================================
Nhập lựa chọn của bạn: ''')
    match choice:
        case '1':
            main.show_all()
        case '2':
            main.add_product()
        case '3':
            main.update_product()
        case '4':
            main.delete_product()
        case '7':
            print("Thoát chương trình")
            break
        case _:
            print('Lựa chọn không hợp lệ')