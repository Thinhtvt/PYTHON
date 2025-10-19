def la_so_hoan_hao(n):
    """Hàm kiểm tra số hoàn hảo"""
    if n <= 1:
        return False  # số <= 1 không thể là số hoàn hảo
    
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    
    return tong_uoc == n


# --- Chương trình chính ---
print("Các số hoàn hảo từ 1 đến 10000 là:")

for num in range(1, 10001):
    if la_so_hoan_hao(num):
        print(num)
