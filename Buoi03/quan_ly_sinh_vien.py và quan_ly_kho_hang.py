# Hoạt động 6: Mini project 1 - Quản lý danh sách sinh viên bằng List
danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]
print("Danh sách ban đầu:")
for diem, ten in danh_sach_sv:
    print(ten, "-", diem)

# Thêm sinh viên
danh_sach_sv.append((8.0, "Em"))
# Xóa sinh viên
danh_sach_sv.remove((7.0, "Binh"))
# Sửa điểm sinh viên đầu tiên
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])
# Kiểm tra sinh viên
print("\nChi có trong danh sách không?", (9.2, "Chi") in danh_sach_sv)

# Sắp xếp tăng dần
danh_sach_sv.sort()
print("\nDanh sách tăng dần:")
for diem, ten in danh_sach_sv:
    print(ten, "-", diem)

# Sắp xếp giảm dần
danh_sach_sv.sort(reverse=True)
print("\nDanh sách giảm dần:")
for diem, ten in danh_sach_sv:
    print(ten, "-", diem)

# Hoạt động 7: Mini project 2 - Quản lý kho hàng + Tổng kết
kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5)
]
print("Danh sách ban đầu:")
for ten, gia, so_luong in kho_hang:
    print(ten, gia, so_luong)

# Thêm sản phẩm
kho_hang.append(("Tai nghe", 300000, 15))
print("\nSau khi thêm:")
for ten, gia, so_luong in kho_hang:
    print(ten, gia, so_luong)

# Xóa sản phẩm
kho_hang.remove(("Chuot", 150000, 20))
print("\nSau khi xóa:")
for ten, gia, so_luong in kho_hang:
    print(ten, gia, so_luong)

# Tính tổng giá trị kho hàng
tong_gia_tri = 0
for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print("\nTổng giá trị kho hàng:", tong_gia_tri, "VND")