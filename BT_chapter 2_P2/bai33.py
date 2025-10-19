# Nhập chuỗi từ người dùng
text = input("Nhập một chuỗi cần kiểm tra: ")

# Chuyển hết về chữ thường cho công bằng (tránh phân biệt hoa thường)
text = text.lower()

# Tạo biến cờ để kiểm tra
is_palindrome = True

# Dùng vòng lặp để so sánh ký tự đầu và cuối
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break

# Hiển thị kết quả
if is_palindrome:
    print(f"✅ Chuỗi '{text}' là một Palindrome!")
else:
    print(f"❌ Chuỗi '{text}' không phải là Palindrome.")
