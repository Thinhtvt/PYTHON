# Bài 12
meal_cost = float(input("Nhập chi phí bữa ăn: "))

tip = meal_cost * 0.18
tax = meal_cost * 0.05
total = meal_cost + tip + tax

print("Tiền boa:", tip)
print("Thuế:", tax)
print("Tổng cộng:", total)
