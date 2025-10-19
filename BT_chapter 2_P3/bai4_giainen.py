import zipfile
import os

def giai_nen(ten_zip, thu_muc_dich):
    if not os.path.exists(ten_zip):
        print(f"⚠️ File nén {ten_zip} không tồn tại.")
        return
    with zipfile.ZipFile(ten_zip, 'r') as zipf:  # 'r' = read
        zipf.extractall(thu_muc_dich)
        print(f"🎯 Đã giải nén tất cả file vào thư mục: {thu_muc_dich}")

# Ví dụ sử dụng
giai_nen('data.zip', 'output_folder')
