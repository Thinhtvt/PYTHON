import math  # để dùng hằng số pi

# Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính đáy hình trụ (r): "))
h = float(input("Nhập chiều cao hình trụ (h): "))

# Công thức tính thể tích hình trụ
V = math.pi * (r ** 2) * h

# In kết quả
print(f"Thể tích hình trụ là: {V:.2f}")
