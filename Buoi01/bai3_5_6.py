# Bài 3.1: Bài 3.1 – Soi lỗi đặt tên
# Cho danh sách định danh sau, sinh viên xác định định danh nào hợp lệ, định danh nào sai và giải thích lý do:
# 1diem gia-tri _tam_thoi Diem_TB
# class so luong MAX_SPEED diemTB
# 2024_data tong$ sinhVien1

# 1. 1diem => bắt đầu bằng số => sai.
# 2. gia-triSai => chứa dấu gạch ngang (-)=> sai.
# 3. _tam_thoi: Hợp lệ
# 4. Diem_TB: Hợp lệ về cú pháp nhưng chưa đúng chuẩn PEP8.
# 5. class => Sai vì là từ khóa của Python.
# 6. so luong => chứa dấu cách => sai.
# 7. MAX_SPEED: Hợp lệ vì đúng kiểu đặt tên hằng số.
# 8. diemTB: Hợp lệ về cú pháp nhưng chưa đúng chuẩn PEP8.
# 9. 2024_data => bắt đầu bằng số => sai.
# 10. tong$ => chứa ký tự đặc biệt $ => sai.
# 11. sinhVien1: Hợp lệ về cú pháp nhưng chưa đúng chuẩn PEP8.

# Bài 3.2: Áp dụng PEP 8
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Họ tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)

# Bài 5.1:  Toán tử số học:
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
# Sự khác nhau giữa / và //
# / là phép chia thông thường, kết quả thường là số thập phân.
# // là phép chia lấy phần nguyên

# Sự khác nhau giữa % và **
# % là phép chia lấy phần dư
# ** là phép lũy thừa

# Bài 5.2: Toán tử so sánh & logic
diem = 6.5
tuoi = 20
print("Điểm đạt loại Khá:", diem >= 6.5 and diem < 8.0)
print("Tuổi chưa đủ 18 hoặc trên 60:", tuoi < 18 or tuoi > 60)
print("Phủ định:", not (tuoi < 18 or tuoi > 60))

# Bài 5.3: Toán tử gán & toán tử đặc biệt
x = 10

x += 5
print("Sau khi x += 5:", x)
x -= 3
print("Sau khi x -= 3:", x)
x *= 2
print("Sau khi x *= 2:", x)
x /= 4
print("Sau khi x /= 4:", x)
x //= 2
print("Sau khi x //= 2:", x)
x **= 3
print("Sau khi x **= 3:", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không:", 3 in danh_sach)
a = danh_sach
b = danh_sach
print("a và b có cùng tham chiếu không:", a is b)


# Bài 5.4: Độ ưu tiên toán tử
# Dự đoán kết quả:50, 80, true
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

# Bài 6: Biến & Dynamic typing
# Bài tập 6.1: Khai báo lần lượt các biến với nhiều kiểu dữ liệu khác nhau và in kiểu bằng type()
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))
# Vì sao cùng một biến bien có thể mang nhiều kiểu dữ liệu khác nhau trong Python?
# Trong Python, biến không cần khai báo kiểu dữ liệu trước.Kiểu dữ liệu được xác định dựa vào giá trị mà biến đang tham chiếu tới. 
# Vì vậy, biến bien có thể lần

# Bài tập 6.2 – Mini bài toán tổng hợp:
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0
dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))