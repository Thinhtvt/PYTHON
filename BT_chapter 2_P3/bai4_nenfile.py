import zipfile
import os

def nen_file(ten_zip, danh_sach_file):
    with zipfile.ZipFile(ten_zip, 'w') as zipf:  # 'w' = write, tạo file nén mới
        for file in danh_sach_file:
            if os.path.exists(file):              # kiểm tra file có tồn tại không
                zipf.write(file)
                print(f"✅ Đã nén: {file}")
            else:
                print(f"⚠️ File {file} không tồn tại, bỏ qua.")
    print(f"\n🎉 Đã tạo file nén: {ten_zip}")

# Ví dụ sử dụng
danh_sach = ['f1.txt', 'f2.txt', 'f3.txt']
nen_file('data.zip', danh_sach)
