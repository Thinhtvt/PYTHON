# Nhập một chữ cái từ người dùng
letter = input("Nhập một chữ cái: ").lower()

# Kiểm tra và hiển thị kết quả
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("Chữ cái bạn nhập là nguyên âm.")
elif letter == 'y':
    print("Chữ cái 'y' có thể là nguyên âm hoặc phụ âm.")
else:
    print("Chữ cái bạn nhập là phụ âm.")
