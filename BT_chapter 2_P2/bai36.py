# Tạo danh sách rỗng để lưu các số
numbers = []

print("Nhập các số nguyên (nhập 0 để kết thúc):")

while True:
    n = int(input("Nhập số: "))
    if n == 0:  # Khi nhập 0 thì dừng lại
        break
    numbers.append(n)

# Sắp xếp danh sách tăng dần
numbers.sort()

# Hiển thị kết quả
print("\nCác số đã nhập theo thứ tự tăng dần:")
for num in numbers:
    print(num)
