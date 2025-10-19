import math

# Bài 16
vi = float(input("Nhập vận tốc ban đầu v_i (m/s): "))
a = 9.8
d = float(input("Nhập độ cao rơi (m): "))

vf = math.sqrt(vi**2 + 2*a*d)
print("Vận tốc cuối cùng khi chạm đất là:", vf, "m/s")
