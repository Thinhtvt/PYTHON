import zipfile
import os

def nen_tap_tin(ten_zip, danh_sach_tap_tin):
    with zipfile.ZipFile(ten_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for tap_tin in danh_sach_tap_tin:
            if os.path.exists(tap_tin):
                zipf.write(tap_tin, os.path.basename(tap_tin))
                print(f"✅ Đã nén: {tap_tin}")
            else:
                print(f"⚠️ Không tìm thấy tệp: {tap_tin}")
    print(f"\n🎉 Tạo tệp nén '{ten_zip}' thành công!")

# --- Chương trình chính ---
danh_sach = []

print("Nhập tên các tệp muốn nén (nhấn Enter để dừng):")
while True:
    ten_tap_tin = input()
    if ten_tap_tin == "":
        break
    danh_sach.append(ten_tap_tin)

ten_zip = input("Nhập tên file zip muốn tạo (ví dụ: output.zip): ")

nen_tap_tin(ten_zip, danh_sach)
