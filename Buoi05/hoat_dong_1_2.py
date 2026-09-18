# Hoạt động 1
# Bài tập 1.1- if đơn và if-else
tuoi =16
if tuoi >=18:
    print("Đã đủ tuổi trưởng thành")
if tuoi >=18:
    print("Được phép đăng ký xe máy")
else:
    print("Chưa đủ tuổi")

#Bài tập 1.2 – if-elif-else:
diem =9.0
if diem >=8.0:
    print("Xếp loại: Giỏi")
elif diem >=6.5:
    print("Xếp loại: Khá")
elif diem >=5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

# Bài tập 1.3 – Điều kiện lồng nhau: 
tuoi =18
co_giay_phep = False
if tuoi >=18:
    if co_giay_phep:
        print("Được phép lái xe")
    else:
        print("Đủ tuổi nhưng chưa có giấy phép")
else:
    print("Chưa đủ tuổi lái xe")

# Bài tập 1.4 – Biểu thức điều kiện rút gọn (conditional expression)
diem = 9.0
ket_qua = "Dat" if diem >= 5.0 else "Khong dat" 
print("Kết quả: ",ket_qua) 
so = -9 
tri_tuyet_doi = so if so >= 0 else -so 
print("Giá trị tuyệt đối: ",tri_tuyet_doi)

# Hoạt động 2
# Bài tập 2.1 – Xếp loại học lực đầy đủ
ho_ten = "Đinh Bảo Linh" 
diem_toan, diem_ly, diem_hoa = 8.6, 8.5, 9.0
dtb = round((diem_toan + diem_ly + diem_hoa) / 3, 2) 
if dtb >= 8.0: 
    xep_loai = "Giỏi" 
elif dtb >= 6.5: 
    xep_loai = "Khá" 
elif dtb >= 5.0: 
   xep_loai = "Trung bình" 
else: 
    xep_loai = "Yếu" 
print(f"{ho_ten} - DTB: {dtb} - Xep loai: {xep_loai}")
print("\n")

# Bài tập 2.2 – Tìm số lớn nhất trong 3 số nhập vào
a = float(input("Nhập số thứ nhất: ")) 
b = float(input("Nhập số thứ hai: ")) 
c = float(input("Nhập số thứ ba: ")) 
if a >= b and a >= c: 
    lon_nhat = a 
elif b >= a and b >= c: 
    lon_nhat = b 
else: 
    lon_nhat = c 
print("Số lớn nhất: ", lon_nhat)

