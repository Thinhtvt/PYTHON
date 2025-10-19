filename = 'alice.txt'  # ⚡ nên khai báo tên file ra biến riêng

try:
    with open(filename) as f_obj:  # Mở file 'alice.txt'
        contents = f_obj.read()    # Đọc toàn bộ nội dung file
except FileNotFoundError:          # Nếu file không tồn tại
    msg = "File " + filename + " không tồn tại."
    print(msg)
else:
    words = contents.split()       # Cắt nội dung thành danh sách các từ
    num_words = len(words)         # Đếm số lượng từ
    print("File " + filename + " có " + str(num_words) + " từ.")
