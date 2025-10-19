def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isupper():
            base = 65  # 'A'
            if mode == 'decode':  # Giải mã thì dịch ngược
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += chr((ord(char) - base + shift) % 26 + base)
        elif char.islower():
            base = 97  # 'a'
            if mode == 'decode':
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


# --- Giao diện người dùng ---
print("=== 🔐 MÃ HÓA / GIẢI MÃ MÃ CAESAR 🔐 ===")
mode = input("Bạn muốn 'encode' (mã hóa) hay 'decode' (giải mã)? ").lower()
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự cần dịch chuyển: "))

# Gọi hàm thực hiện
output = caesar_cipher(message, shift, mode)

print("\n🧾 Kết quả:", output)
