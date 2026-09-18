# Hoạt động 7
import random
print("====================================")
print(" TRÒ CHƠI ĐOÁN SỐ ")
print(" Tối đa 7 lượt đoán ")
print("====================================")

so_can_doan = random.randint(1,100)
so_luot_toi_da = 7
luot_hien_tai = 0

while luot_hien_tai < so_luot_toi_da:
    luot_hien_tai += 1
    so_doan = int(input(f"Luot {luot_hien_tai}/{so_luot_toi_da} - Nhập số bạn đoán (1-100): "))
    if so_doan == so_can_doan:
        print("Chính xác!")
        print(f"Bạn đã đoán đúng sau {luot_hien_tai} lượt.")
        break
    elif so_doan < so_can_doan:
        print("Gợi ý: Số cần đoán LỚN HƠN số bạn vừa nhập.")
    else:
        print("Gợi ý: Số cần đoán NHỎ HƠN số bạn vừa nhập.")

else:
    print("Bạn đã hết lượt đoán.")
    print("Số đúng là:", so_can_doan)

print("Cảm ơn!")