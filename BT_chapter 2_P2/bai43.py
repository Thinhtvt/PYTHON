def compare_strings(str1, str2):
    if len(str1) > len(str2):
        print("Chuỗi dài hơn là:", str1)
    elif len(str2) > len(str1):
        print("Chuỗi dài hơn là:", str2)
    else:
        print("Hai chuỗi có cùng độ dài:")
        print(str1)
        print(str2)

# Nhập hai chuỗi từ người dùng
s1 = input("Nhập chuỗi thứ nhất: ")
s2 = input("Nhập chuỗi thứ hai: ")

# Gọi hàm so sánh
compare_strings(s1, s2)
