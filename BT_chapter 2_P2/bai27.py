# Tạo bảng tra cứu số cạnh - tên hình
shapes = {
    3: "tam giác",
    4: "tứ giác",
    5: "ngũ giác",
    6: "lục giác",
    7: "thất giác",
    8: "bát giác",
    9: "cửu giác",
    10: "thập giác"
}

# Nhập số cạnh
sides = int(input("Nhập số cạnh của hình: "))

# Kiểm tra và in kết quả
if sides in shapes:
    print(f"Đó là hình {shapes[sides]}.")
else:
    print("Lỗi: Chỉ hỗ trợ hình có từ 3 đến 10 cạnh.")
