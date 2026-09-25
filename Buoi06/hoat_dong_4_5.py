# Hoạt động 4: Phạm vi biến – local, global, từ khóa global
print("===== Hoạt động 4 =====")
so_luot_truy_cap = 0 # bien global
def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1
def vi_du_bien_local():
    so_luot_truy_cap = 100 # day la bien LOCAL, khac voi bien global cung ten
    print("Bên trong hàm, biến local =", so_luot_truy_cap)
tang_luot_truy_cap()
tang_luot_truy_cap()
tang_luot_truy_cap()
tang_luot_truy_cap()
print("Số lượt truy cập (global):", so_luot_truy_cap)
vi_du_bien_local()
print("Sau khi gọi hàm, biến global vẫn là:", so_luot_truy_cap)

# Hoạt động 5: Hàm lambda kết hợp map(), filter(), sorted()
print("\n===== Bài tập 5.1 =====")
danh_sach_so = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print("Danh sách ban đầu: ", danh_sach_so)
print("Bình phương: ",binh_phuong)


print ("\n===== Bài tập 5.2 =====")
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print("Số chẵn: ",so_chan)

print ("\n===== Bài tập 5.3 =====")
danh_sach_sv = [
    {"Tên": "An", "điểm": 8.5},
    {"Tên": "Trang", "điểm": 7.0},
    {"Tên": "Linh", "điểm": 9.2},
    ]
sap_xep_theo_diem = sorted(
    danh_sach_sv, key=lambda sv: sv["điểm"]
    )
sap_xep_giam_dan = sorted(
    danh_sach_sv, key=lambda sv: sv["điểm"], reverse=True
    )
print("--- Theo điểm ---")
for sv in sap_xep_theo_diem:
    print(sv["Tên"], "-", sv["điểm"])
print("--- Giảm dần ---")
for sv in sap_xep_giam_dan:
    print(sv["Tên"], "-", sv["điểm"])