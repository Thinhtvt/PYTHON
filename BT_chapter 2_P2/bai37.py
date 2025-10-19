words = []  # Danh sách lưu các từ
print("Nhập các từ (nhấn Enter trên dòng trống để kết thúc):")

while True:
    word = input()
    if word == "":  # Dừng khi nhập dòng trống
        break
    if word not in words:  # Chỉ thêm nếu chưa có
        words.append(word)

print("\nCác từ duy nhất bạn đã nhập:")
for w in words:
    print(w)
