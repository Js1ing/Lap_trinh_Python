# Bài tập 4.1 - Ép kiểu tường minh
chuoi_so = "25" 
so = int(chuoi_so) 
print(so, type(so)) 
so_thuc = float("3.14") 
print(so_thuc, type(so_thuc)) 
danh_sach = list((1, 2, 3)) # tuple -> list 
bo_ba = tuple([4, 5, 6]) # list -> tuple 
tap_hop = set([1, 2, 2, 3, 3, 3]) # list -> set (tu loai bo trung lap) 
tu_dien = dict([("a", 1),("b", 2)]) # list cac tuple -> dict 
print("List: ", danh_sach)
print("Tuple: ", bo_ba)
print("Set: ", tap_hop)
print("Dictionary: ", tu_dien)

# Bài 4.2 – Trường hợp gây lỗi
# int("abc") 
# int("3.14")
so_hop_le = int(float("3.14")) ## cach lam dung: ep qua float truoc 
print("Sau khi ép đúng:", so_hop_le)

# Bài tập 4.3 - Chuyển đổi ngầm định
ket_qua = 5 + 2.5 # int + float -> Python tu dong chuyen thanh float 
print(ket_qua, type(ket_qua)) 
ket_qua_2 = "Diem: " + str(8.5) # phai ep str() tuong minh, Python KHONG tu dong noi  str voi so 
print(ket_qua_2)
