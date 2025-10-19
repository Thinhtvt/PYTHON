def print_square_list():
    # Tạo danh sách rỗng
    squares = []

    # Thêm các bình phương từ 1 đến 20 vào danh sách
    for i in range(1, 21):
        squares.append(i ** 2)

    # In kết quả
    print(squares)

# Gọi hàm
print_square_list()
