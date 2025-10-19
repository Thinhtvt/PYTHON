import math

# Bài 8: Tính diện tích tam giác đều theo định lý Heron
a = float(input("Nhập cạnh của tam giác đều: "))

p = (a + a + a) / 2
S = math.sqrt(p * (p - a) * (p - a) * (p - a))

print("Diện tích tam giác đều là:", S)
