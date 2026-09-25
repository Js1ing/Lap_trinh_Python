# Hoạt động 1: Hàm cơ bản – def, tham số, return
print("===== Bài tập 1.1 =====")
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
        return a
print("USCLN:")
print("24 và 36 =", uscln(24, 36))
print("15 và 45 =", uscln(15, 45))
print("100 và 25 =", uscln(100, 25))

def bscnn(a, b):
    return a * b // uscln(a, b)
print("\nBSCNN:")
print("4 và 6 =", bscnn(4, 6))
print("8 và 12 =", bscnn(8, 12))
print("9 và 15 =", bscnn(9, 15))

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
print("\nSo Nguyen To:")
print("29:", kiem_tra_nguyen_to(29))
print("17:", kiem_tra_nguyen_to(17))
print("20:", kiem_tra_nguyen_to(20))

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
print("\nSo Hoan Thien:")
print("28:", kiem_tra_so_hoan_thien(28))
print("6:", kiem_tra_so_hoan_thien(6))
print("20:", kiem_tra_so_hoan_thien(20)) # 28 = 1 + 2 + 4 + 7 + 14

print("\n===== Bài tập 1.2 =====")
def in_loi_chao(ten):
    print(f"Xin chào, {ten}!")
    return # ham khong tra ve gia tri (tra ve None)
def chia_lay_thuong_du(a, b):
    return a // b, a % b # tra ve nhieu gia tri qua tuple
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thương: {thuong}, dư: {du}")

in_loi_chao("Linh")
thuong, du = chia_lay_thuong_du(50, 9)
print(f"Thương: {thuong}, dư: {du}")

# Hoạt động 2: Tham số mặc định & tham số từ khóa
print("\n===== Hoạt động 2 =====")
def gioi_thieu(ten, tuoi=18, lop="Chưa rõ"):
    print(f"Tên: {ten} - Tuổi: {tuoi} - Lớp: {lop}")
gioi_thieu("An") # dung het gia tri mac dinh
gioi_thieu("Binh", 20) # ghi de tuoi
gioi_thieu("Chi", lop="CNTT01") # dung tham so tu khoa, bo qua tuoi
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19) # thu tu tham so tu khoa co the dao lon

# Hoạt động 3: Tham số linh hoạt – *args và **kwargs
print("\n===== Bài tập 3.1 =====")
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong(8, 18, 28, 38))
print(tinh_tong()) # khong truyen so nao -> tra ve 0

print("\n===== Bài tập 3.2 =====")
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Họ tên: {ho_ten} - Tuổi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"{khoa}: {gia_tri}")
in_thong_tin("Nguyễn Văn A",21,lop="CNTT01",que_quan="Hà Nội")
in_thong_tin("Đinh Bảo Linh",20,email="linh123@gmail.com")
in_thong_tin("Nguyễn Hải Quỳnh",19,lop="CNTT02",email="c@example.com",que_quan="Nam Định")