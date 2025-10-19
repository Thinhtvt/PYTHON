def print_first5_squares():
    # Tạo danh sách rỗng
    squares = []

    # Dùng vòng lặp để tính bình phương từ 1 đến 20
    for i in range(1, 21):
        squares.append(i ** 2)

    # In 5 phần tử đầu tiên (dùng slicing)
    print(squares[:5])

# Gọi hàm
print_first5_squares()
