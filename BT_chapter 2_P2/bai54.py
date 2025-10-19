def dinh_dang_danh_sach(words):
    """Hàm định dạng danh sách từ theo quy tắc tiếng Anh"""
    if len(words) == 0:
        return ""  # danh sách rỗng thì trả về chuỗi rỗng
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return f"{words[0]} and {words[1]}"
    else:
        # Nối các phần tử trừ phần cuối bằng dấu phẩy
        return ", ".join(words[:-1]) + " and " + words[-1]


# --- Chương trình chính ---
words = []  # danh sách lưu từ người dùng nhập

print("Nhập từng từ (nhấn Enter để dừng):")
while True:
    word = input()
    if word == "":
        break
    words.append(word)

result = dinh_dang_danh_sach(words)
print("\nDanh sách được định dạng là:")
print(result)
