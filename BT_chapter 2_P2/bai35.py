# Nhập chuỗi số từ người dùng
numbers = input("Nhập các số cách nhau bằng dấu phẩy: ")

# Tách chuỗi thành danh sách và chuyển từng phần tử thành số nguyên
num_list = [int(x) for x in numbers.split(',')]

# Lọc ra các số lẻ
odd_numbers = [n for n in num_list if n % 2 != 0]

# Hiển thị kết quả
print("Các số lẻ là:", odd_numbers)
