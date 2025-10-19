# Bài 11
length = float(input("Nhập chiều dài cánh đồng (m): "))
width = float(input("Nhập chiều rộng cánh đồng (m): "))

area_m2 = length * width
area_acre = area_m2 / 43560

print("Diện tích cánh đồng là:", area_acre, "mẫu Anh")
