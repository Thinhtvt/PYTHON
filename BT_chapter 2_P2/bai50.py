import random

def tao_mat_khau():
    # Bước 1: tạo độ dài ngẫu nhiên từ 7 đến 10
    do_dai = random.randint(7, 10)
    
    # Bước 2: tạo mật khẩu bằng cách chọn ngẫu nhiên các ký tự ASCII (33–126)
    mat_khau = ''.join(chr(random.randint(33, 126)) for _ in range(do_dai))
    
    # Bước 3: trả về mật khẩu
    return mat_khau

# Chương trình chính
print("Mật khẩu ngẫu nhiên được tạo là:", tao_mat_khau())
