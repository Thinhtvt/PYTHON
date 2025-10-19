def danh_sach_con(lst):
    """Hàm trả về mọi danh sách con có thể có"""
    result = [[]]  # danh sách rỗng luôn là một danh sách con
    n = len(lst)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(lst[i:j])
    
    return result


# --- Chương trình chính ---
my_list = [1, 2, 3]
print("Tất cả các danh sách con của", my_list, "là:")
print(danh_sach_con(my_list))
