def print_list_exclude_first5():
    # Tạo danh sách bình phương các số từ 1 đến 20
    squares = [x ** 2 for x in range(1, 21)]
    # In ra tất cả phần tử trừ 5 phần tử đầu tiên
    print(squares[5:])

print_list_exclude_first5()
