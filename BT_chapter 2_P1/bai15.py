# Bài 15
M = float(input("Nhập khối lượng nước (gam): "))
delta_T = float(input("Nhập độ thay đổi nhiệt độ ΔT (°C): "))

C = 4.186  # J/gC
Q = M * C * delta_T  # Joules

# Đổi sang kWh
Q_kWh = Q * 2.7778e-7

# Tính chi phí
cost = Q_kWh * 8.9  # cent

print("Năng lượng cần thiết (J):", Q)
print("Năng lượng cần thiết (kWh):", Q_kWh)
print("Chi phí (cent):", cost)
