def count_words(filename):  # Định nghĩa hàm đếm số từ
    try:
        with open(filename) as f_obj:   # Mở file
            contents = f_obj.read()     # Đọc nội dung file
    except FileNotFoundError:           # Nếu file không tồn tại
        msg = "File " + filename + " không tồn tại."
        print(msg)
    else:                               # Nếu đọc file thành công
        words = contents.split()        # Tách nội dung thành các từ
        num_words = len(words)          # Đếm số từ
        print("File " + filename + " có " + str(num_words) + " từ.")

# Danh sách các file cần xử lý
filenames = ['f1.txt', 'f2.txt', 'f3.txt']

# Gọi hàm cho từng file trong danh sách
for filename in filenames:
    count_words(filename)
