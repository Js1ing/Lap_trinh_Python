quan_ly_diem = { 
 "Nguyễn Hải Anh": [8.0, 7.5, 9.0], 
 "Trần Như Quỳnh": [6.0, 6.5, 5.5], 
 "Lê Trâm Anh": [9.0, 9.5, 8.5],
} 
# Them sinh vien moi 
quan_ly_diem["Phạm Bảo Linh"] = [7.0, 8.0, 7.5] 
# Sua diem mon dau tien cua mot sinh vien 
quan_ly_diem["Trần Như Quỳnh"][0] = 7.0 
diem_trung_binh = {} 

for ho_ten, danh_sach_diem in quan_ly_diem.items(): 
   diem_trung_binh[ho_ten] = round(sum(danh_sach_diem) / len(danh_sach_diem), 2) 
print("== BẢNG ĐIỂM TRUNG BÌNH ==") 
for ho_ten, dtb in diem_trung_binh.items(): 
 dat_loai_gioi = dtb >= 8.0 
 print(f"{ho_ten:<15} - DTB: {dtb:<5} - Đạt Loại Giỏi? {dat_loai_gioi}")
