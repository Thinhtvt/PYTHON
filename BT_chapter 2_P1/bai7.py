import math

# Bài 7: Tính diện tích tam giác theo công thức cạnh và góc
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

A = float(input("Nhập góc A (rad): "))
B = float(input("Nhập góc B (rad): "))
C = float(input("Nhập góc C (rad): "))

# Có thể dùng công thức: S = 1/2 * a * b * sin(C)
S = 0.5 * a * b * math.sin(C)

print("Diện tích tam giác là:", S)
