def print_last5_squares():
    # Tạo danh sách rỗng
    squares = []

    # Dùng vòng lặp để tính bình phương từ 1 đến 20
    for i in range(1, 21):
        squares.append(i ** 2)

    # In 5 phần tử cuối cùng (dùng slicing)
    print(squares[-5:])

# Gọi hàm
print_last5_squares()
