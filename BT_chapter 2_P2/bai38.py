print("Nhập các số nguyên (nhấn Enter trên dòng trống để kết thúc):")

numbers = []

while True:
    line = input().strip()  # loại bỏ khoảng trắng đầu/cuối
    if line == "":          # dừng khi dòng trống
        break
    try:
        numbers.append(int(line))
    except ValueError:
        print("⚠️ Vui lòng nhập số nguyên hợp lệ!")
        continue

negatives = [n for n in numbers if n < 0]
zeros = [n for n in numbers if n == 0]
positives = [n for n in numbers if n > 0]

result = negatives + zeros + positives

print("\nCác giá trị được sắp xếp theo quy tắc:")
for n in result:
    print(n)
