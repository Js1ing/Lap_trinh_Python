def them_sach(danh_sach, ma, ten, gia, soluong):
    sach = {
        "MaSach": ma,
        "TenSach": ten,
        "Gia": gia,
        "SoLuong": soluong
    }
    danh_sach.append(sach)

def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua = []
    tu_khoa = tu_khoa.lower()

    for sach in danh_sach:
        ten_sach = sach["TenSach"].lower()
        if tu_khoa in ten_sach:
            ket_qua.append(sach)

    return ket_qua

def tong_gia_tri_kho_sach(danh_sach):
    tong = 0
    for sach in danh_sach:
        gia_tri = sach["Gia"] * sach["SoLuong"]
        tong = tong + gia_tri

    return tong

def main():
    danh_sach = []

    while True:
        print("\n===== QUẢN LÝ SÁCH THƯ VIỆN =====")
        print("1. Thêm sách")
        print("2. Tìm kiếm theo tên")
        print("3. Xem tổng giá trị kho sách")
        print("4. Thoát chương trình")
        lua_chon = input("Nhập lựa chọn: ").strip()

        if lua_chon == "1":
            ma = input("Nhập mã sách: ").strip()
            ten = input("Nhập tên sách: ").strip()
            try:
                gia = int(input("Nhập giá sách: "))
                soluong = int(input("Nhập số lượng: "))
            except ValueError:
                print("Giá và số lượng phải là số nguyên.")
            else:
                them_sach(danh_sach, ma, ten, gia, soluong)
                print("Đã thêm sách.")

        elif lua_chon == "2":
            tu_khoa = input("Nhập từ khóa tìm kiếm: ").strip()
            ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)
            if len(ket_qua) == 0:
                print("Không tìm thấy sách phù hợp.")
            else:
                print("Kết quả tìm kiếm:")
                for sach in ket_qua:
                    ma = sach["MaSach"]
                    ten = sach["TenSach"]
                    gia = sach["Gia"]
                    soluong = sach["SoLuong"]
                    print(f"{ma} - {ten} - {gia}đ - SL: {soluong}")

        elif lua_chon == "3":
            tong = tong_gia_tri_kho_sach(danh_sach)
            print("Tổng giá trị kho sách:", tong, "đồng")

        elif lua_chon == "4":
            print("Đã thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Hãy nhập từ 1 đến 4.")

if __name__ == "__main__":
    main()