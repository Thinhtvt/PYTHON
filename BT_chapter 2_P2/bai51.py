def kiem_tra_mat_khau(password):
    # Kiểm tra độ dài
    if len(password) < 8:
        return False

    # Biến cờ kiểm tra
    co_chu_hoa = False
    co_chu_thuong = False
    co_so = False

    # Duyệt từng ký tự trong mật khẩu
    for ky_tu in password:
        if ky_tu.isupper():
            co_chu_hoa = True
        elif ky_tu.islower():
            co_chu_thuong = True
        elif ky_tu.isdigit():
            co_so = True

    # Mật khẩu tốt khi đủ cả 3 điều kiện
    return co_chu_hoa and co_chu_thuong and co_so


# Chương trình chính
mat_khau = input("Nhập mật khẩu cần kiểm tra: ")

if kiem_tra_mat_khau(mat_khau):
    print("✅ Mật khẩu TỐT!")
else:
    print("❌ Mật khẩu CHƯA tốt, hãy thêm chữ hoa, chữ thường, và số nhé!")
