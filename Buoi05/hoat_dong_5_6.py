# Hoạt động 5
print("Bài tập 5.1 - pass")
diem = 6.5 
if diem >= 8.0: 
   pass # chua cai dat logic cho truong hop nay, se bo sung sau 
elif diem >= 5.0: 
  print("Đạt yêu cầu") 
else: 
  pass

print ("Bài tập 5.2 - break")
so = int(input("Nhập số: "))
la_so_nguyen_to = True 
if so < 2: 
   la_so_nguyen_to = False 
else: 
  for i in range(2, so):
    if so % i == 0: 
       la_so_nguyen_to = False 
       break # thoat ngay khi tim thay uoc so, khong can kiem tra tiep 
print(f"{so} co phai so nguyen to khong? {la_so_nguyen_to}")

print("Bài tập 5.3 – break: Tìm số nguyên tố đầu tiên lớn hơn n")
n = int(input("Nhap n: "))
so_hien_tai = n + 1
while True:
    la_so_nguyen_to = True
    for i in range(2, so_hien_tai):
        if so_hien_tai % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        break
    so_hien_tai += 1
print("So nguyen to dau tien lon hon", n, "la", so_hien_tai)

print("Bài tập 5.4 – continue")
danh_sach = [5, -3, 8, 0, -1, 12, 7, -9] 
danh_sach_hop_le = [] 
for so in danh_sach: 
   if so <= 0: 
      continue # bo qua cac so khong duong, khong them vao danh sach ket qua  
   danh_sach_hop_le.append(so) 
print("Các số hợp lệ (dương):", danh_sach_hop_le)

# Hoạt động 6
print("Bài tập 6.1 – Tam giác sao")
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

print("Bài tập 6.2 – Hình thoi sao")
n = 4 
# Nua tren cua hinh thoi 
for i in range(1, n + 1): 
   print(" " * (n - i) + "*" * (2 * i - 1)) 
# Nua duoi cua hinh thoi 
for i in range(n - 1, 0, -1): 
   print(" " * (n - i) + "*" * (2 * i - 1))
