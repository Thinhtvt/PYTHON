# Định nghĩa hàm tính giai thừa
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Nhập số từ người dùng
n = int(input("Nhập một số nguyên n: "))

# Tính giai thừa và in kết quả
print(f"Giai thừa của {n} là: {factorial(n)}")
