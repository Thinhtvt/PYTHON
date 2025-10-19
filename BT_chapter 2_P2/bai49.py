def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # chỉ cần kiểm tra đến căn bậc hai của n
        if n % i == 0:
            return False
    return True

# Chương trình chính
so = int(input("Nhập một số nguyên: "))

if la_so_nguyen_to(so):
    print(so, "là số nguyên tố.")
else:
    print(so, "không phải là số nguyên tố.")
