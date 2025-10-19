import math

# Bài 14
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print("Tổng a + b =", a + b)
print("Hiệu a - b =", a - b)
print("Tích a * b =", a * b)
if b != 0:
    print("Thương a / b =", a / b)
    print("Phần dư a % b =", a % b)
else:
    print("Không thể chia cho 0")

if a > 0:
    print("log10(a) =", math.log10(a))
else:
    print("Không tính được log10(a) khi a <= 0")

print("a^b =", a ** b)
