# Nhập tên tháng từ người dùng
month = input("Nhập tên tháng (ví dụ: January): ").strip().lower()

# Kiểm tra và in ra số ngày tương ứng
if month in ("january", "march", "may", "july", "august", "october", "december"):
    print("Tháng này có 31 ngày.")
elif month in ("april", "june", "september", "november"):
    print("Tháng này có 30 ngày.")
elif month == "february":
    print("Tháng 2 có 28 hoặc 29 ngày.")
else:
    print("Tên tháng không hợp lệ. Vui lòng nhập lại!")
