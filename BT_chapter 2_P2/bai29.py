# Nhập độ dài 3 cạnh từ người dùng
a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))

# Kiểm tra có phải tam giác hợp lệ không
if a + b > c and a + c > b and b + c > a:
    # Phân loại tam giác
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or a == c or b == c:
        print("Đây là tam giác cân.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Ba cạnh này không tạo thành một tam giác hợp lệ.")
