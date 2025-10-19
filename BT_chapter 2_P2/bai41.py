# Cho trước tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Tạo tuple mới chỉ chứa số chẵn
even_tup = tuple(x for x in tup if x % 2 == 0)

# In kết quả
print(even_tup)
