import csdl_phim as db
db.tao_bang_neu_chua_co()

db.them_phim("Conan Movie 27", "Chika Nagaoka", "Hoat hinh", 2024)
db.them_phim("Mai", "Tran Thanh", "Tinh cam", 2024)
db.them_phim("Inception", "Christopher Nolan", "Khoa hoc vien tuong", 2010)
db.them_phim("Titanic", "James Cameron", "Tinh cam", 1997)

print("Danh sach phim:")
for phim in db.lay_toan_bo_phim():
    print(phim)
    
db.danh_dau_da_xem(1)
print("\nSau khi danh dau da xem id=1:")
for phim in db.lay_toan_bo_phim():
    print(phim)

db.xoa_phim(2)
print("\nSau khi xoa phim id=2:")
for phim in db.lay_toan_bo_phim():
    print(phim)

print("\nThong ke theo the loai:")
print(db.thong_ke_theo_the_loai())
