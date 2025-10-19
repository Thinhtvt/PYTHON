# Nhập số thập phân từ người dùng
decimal = int(input("Nhập một số thập phân (số nguyên): "))

# Dùng hàm bin() để chuyển sang nhị phân và cắt bỏ '0b' ở đầu
binary = bin(decimal)[2:]

# Hiển thị kết quả
print(f"Số {decimal} trong hệ nhị phân là: {binary}")
