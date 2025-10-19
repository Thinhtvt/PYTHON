import zipfile
import os

def giai_nen_tap_tin(ten_zip, thu_muc_dich):
    if not zipfile.is_zipfile(ten_zip):
        print("⚠️ Đây không phải là tệp ZIP hợp lệ!")
        return
    with zipfile.ZipFile(ten_zip, 'r') as zipf:
        zipf.extractall(thu_muc_dich)
        print(f"🎉 Đã giải nén '{ten_zip}' vào thư mục '{thu_muc_dich}'")

# --- Chương trình chính ---
ten_zip = input("Nhập tên tệp zip cần giải nén: ")
thu_muc_dich = input("Nhập thư mục muốn lưu (vd: extracted_files): ")

if not os.path.exists(thu_muc_dich):
    os.makedirs(thu_muc_dich)

giai_nen_tap_tin(ten_zip, thu_muc_dich)
