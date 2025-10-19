def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isupper():  # Nếu là chữ hoa
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():  # Nếu là chữ thường
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Giữ nguyên ký tự không phải chữ
    return result

# Nhập chuỗi từ người dùng
message = input("Nhập tin nhắn cần mã hóa: ")

# Gọi hàm mã hóa
encrypted = caesar_cipher(message)

print("🔒 Tin nhắn sau khi mã hóa:", encrypted)
