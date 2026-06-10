products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def menu():
    print("=" * 50)
    print("QUẢN LÝ CỬA HÀNG - MINISTORE")
    print("=" * 50)
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm mới sản phẩm")
    print("3. Cập nhật giá sản phẩm theo id")
    print("4. Thoát")
    print("=" * 50)
def display_item():
    global products
    if len(products) == 0:
        print("Chua co san pham!!!")
    print("=== DANH SACH SAN PHAM ===")
    print(f"{"ID":<5} | {"TEN SAN PHAM":<20} | {"GIA BAN"}:<15")
    print("-" * 40)
    for item in products:
        print(f"{item['id']:<5} | {item['name']:<20} | {item['price']:<15}")
    print("-" * 40)
def add_item():
    global products
    while True:
        id_input = input("NHAP ID MOI: ").upper()
        if id_input == "":
            print("ID SAN PHAM KHONG DUOC DE TRONG!!!")
            continue
        found = False
        for item in products:
            if id_input.lower() == item["id"].lower():
                print("ID da ton tai")
                found = True
                break

        if not found:
            break 
    while True:
        name_input = input("NHAP TEN SAN PHAM MOI: ")
        if name_input == "":
            print("TEN SAN PHAM KHONG DUOC DE TRONG!!!")
            continue
        break
    while True:
        try:
            price_input = int(input("NHAP GIA BAN SAN PHAM: "))
            if price_input <= 0:
                print("SAN PHAM PHAI LON HON 0")
                continue
            break
        except ValueError:
            print("SAI DU LIEU")
    product = {
        "id":id_input,
        "name":name_input,
        "price":price_input
    }
    products.append(product)
    print("THEM THANH CONG")
def update_price(products_list):
    id_input = input("NHẬP ID SẢN PHẨM CẦN CẬP NHẬT: ").upper()

    found = False
    for item in products_list:
        if item["id"].upper() == id_input:
            while True:
                try:
                    new_price = int(input("NHẬP GIÁ MỚI: "))
                    if new_price <= 0:
                        print("GIÁ PHẢI LỚN HƠN 0!")
                        continue
                    item["price"] = new_price
                    print("Cập nhật giá thành công!")
                    found = True
                    break
                except ValueError:
                    print("SAI ĐỊNH DẠNG, NHẬP SỐ!")

            break

    if not found:
        print(f"Không tìm thấy sản phẩm có mã {id_input}!")
def main():
    while True:
        menu()
        choice = input("Nhập vào chức năng bạn chọn: ")

        match choice:
            case "1":
                display_item()
            case "2":
                add_item()
            case "3":
                update_price()
            case "4":
                print("THOÁT CHƯƠNG TRÌNH")
                break
            case _:
                print("KHÔNG HỢP LỆ")
main()