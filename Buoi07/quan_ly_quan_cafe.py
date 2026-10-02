danh_sach_mon = [
    {"ma_mon": "M101","ten_mon": "Cà phê đen","loai_mon": "Cà phê","gia": 25000,"trang_thai": "Đang bán"},
    {"ma_mon": "M102","ten_mon": "Cà phê sữa","loai_mon": "Cà phê","gia": 30000,"trang_thai": "Đang bán"},
    {"ma_mon": "M103","ten_mon": "Trà đào","loai_mon": "Trà","gia": 35000,"trang_thai": "Đang bán"},
    {"ma_mon": "M104","ten_mon": "Trà sữa","loai_mon": "Trà sữa","gia": 40000,"trang_thai": "Đang bán"}
]

danh_sach_don_hang = []
lich_su_doanh_thu = []

def hien_thi_danh_sach_mon():
    print("\n" + "=" * 75)
    print(f"{'Mã món':<10}{'Tên món':<20}{'Loại món':<15}{'Giá':<15}{'Trạng thái':<15}")
    print("-" * 75)
    for mon in danh_sach_mon:
        print(f"{mon['ma_mon']:<10}"
              f"{mon['ten_mon']:<20}"
              f"{mon['loai_mon']:<15}"
              f"{mon['gia']:<15,} "
              f"{mon['trang_thai']:<15}")
    print("=" * 75)

def tim_mon_theo_ma(ma_mon):
    for mon in danh_sach_mon:
        if mon["ma_mon"] == ma_mon:
            return mon
    return None

def xem_mon_dang_ban():
    mon_dang_ban = [
        mon for mon in danh_sach_mon
        if mon["trang_thai"] == "Đang bán"
    ]
    if len(mon_dang_ban) == 0:
        print("-> Hiện không có món nào đang bán.")
        return
    print("\nCÁC MÓN ĐANG BÁN:")
    for mon in mon_dang_ban:
        print(f" {mon['ma_mon']} - {mon['ten_mon']} - "
              f"{mon['gia']:,} VNĐ")

def them_mon(ma_mon, ten_mon, loai_mon, gia):
    if tim_mon_theo_ma(ma_mon) is not None:
        print(f"-> Mã món {ma_mon} đã tồn tại, không thể thêm.")
        return
    danh_sach_mon.append({
        "ma_mon": ma_mon,
        "ten_mon": ten_mon,
        "loai_mon": loai_mon,
        "gia": gia,
        "trang_thai": "Đang bán"
    })
    print(f"-> Đã thêm món {ten_mon} thành công.")

def dat_mon(ma_mon, ten_khach, so_luong):
    mon = tim_mon_theo_ma(ma_mon)
    if mon is None:
        print(f"-> Không tìm thấy món {ma_mon}.")
        return
    if mon["trang_thai"] != "Đang bán":
        print(f"-> Món {ma_mon} hiện không bán.")
        return
    thanh_tien = mon["gia"] * so_luong
    ma_don = len(danh_sach_don_hang) + 1
    danh_sach_don_hang.append({
        "ma_don": ma_don,
        "ma_mon": ma_mon,
        "ten_mon": mon["ten_mon"],
        "ten_khach": ten_khach,
        "so_luong": so_luong,
        "thanh_tien": thanh_tien,
        "trang_thai": "Chưa thanh toán"
    })
    print(f"-> Đặt món {mon['ten_mon']} cho khách "
          f"{ten_khach} thành công.")
    print(f"-> Thành tiền: {thanh_tien:,} VNĐ")

def thanh_toan_don(ma_don):
    for don in danh_sach_don_hang:
        if don["ma_don"] == ma_don:
            if don["trang_thai"] == "Đã thanh toán":
                print(f"-> Đơn hàng {ma_don} đã thanh toán.")
                return
            lich_su_doanh_thu.append({
                "ma_don": don["ma_don"],
                "ten_khach": don["ten_khach"],
                "ten_mon": don["ten_mon"],
                "so_luong": don["so_luong"],
                "thanh_tien": don["thanh_tien"]
            })
            don["trang_thai"] = "Đã thanh toán"
            print(f"-> Khách {don['ten_khach']} đã thanh toán "
                  f"đơn {ma_don}.")
            print(f"-> Tổng tiền: {don['thanh_tien']:,} VNĐ")
            return
    print(f"-> Không tìm thấy đơn hàng {ma_don}.")

def thong_ke_doanh_thu():
    if len(lich_su_doanh_thu) == 0:
        print("-> Chưa có đơn hàng nào đã thanh toán.")
        return
    tong_doanh_thu = 0
    print("\nLỊCH SỬ DOANH THU:")
    for giao_dich in lich_su_doanh_thu:
        print(f" Đơn {giao_dich['ma_don']} - "
              f"{giao_dich['ten_khach']} - "
              f"{giao_dich['ten_mon']} - "
              f"{giao_dich['so_luong']} món - "
              f"{giao_dich['thanh_tien']:,} VNĐ")
        tong_doanh_thu += giao_dich["thanh_tien"]
    print(f"\n>>> TỔNG DOANH THU: {tong_doanh_thu:,} VNĐ")

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Dữ liệu không hợp lệ, vui lòng nhập số nguyên.")

def hien_thi_menu():
    print("\n===== QUẢN LÝ QUÁN CÀ PHÊ MINI =====")
    print("1. Hiển thị danh sách tất cả món")
    print("2. Xem các món đang bán")
    print("3. Thêm món mới")
    print("4. Đặt món cho khách")
    print("5. Thanh toán đơn hàng")
    print("6. Thống kê doanh thu")
    print("0. Thoát chương trình")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach_mon()
        elif lua_chon == "2":
            xem_mon_dang_ban()
        elif lua_chon == "3":
            ma_mon = input("Nhập mã món mới: ").strip().upper()
            ten_mon = input("Nhập tên món: ").strip()
            loai_mon = input("Nhập loại món: ").strip()
            gia = nhap_so_nguyen("Nhập giá món: ")
            them_mon(ma_mon, ten_mon, loai_mon, gia)
        elif lua_chon == "4":
            ma_mon = input("Nhập mã món cần đặt: ").strip().upper()
            ten_khach = input("Nhập tên khách: ").strip()
            so_luong = nhap_so_nguyen("Nhập số lượng: ")
            dat_mon(ma_mon, ten_khach, so_luong)
        elif lua_chon == "5":
            ma_don = nhap_so_nguyen(
                "Nhập mã đơn hàng cần thanh toán: "
            )
            thanh_toan_don(ma_don)
        elif lua_chon == "6":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Thoát chương trình!")
            break
        else:
            print("-> Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    chay_chuong_trinh()