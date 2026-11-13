import tkinter as tk
from tkinter import messagebox
import Cau1

class UngDungQuanLySach(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý sách thư viện")
        self.geometry("560x520")
        self.resizable(False, False)

        self.danh_sach_sach = [] 
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
       
        khung_nhap = tk.LabelFrame(self, text="Thêm sách mới")
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Mã sách:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.o_nhap_ma = tk.Entry(khung_nhap, width=35)
        self.o_nhap_ma.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Tên sách:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=35)
        self.o_nhap_ten.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Giá:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.o_nhap_gia = tk.Entry(khung_nhap, width=35)
        self.o_nhap_gia.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Số lượng:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.o_nhap_soluong = tk.Entry(khung_nhap, width=35)
        self.o_nhap_soluong.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm sách", command=self.xu_ly_them_sach).grid(row=4, column=0, columnspan=2, pady=10)
        khung_tim = tk.LabelFrame(self, text="Tìm kiếm theo tên")
        khung_tim.pack(pady=5, padx=10, fill="x")

        tk.Label(khung_tim, text="Từ khóa:").grid(row=0, column=0, padx=10, pady=5)
        self.o_nhap_tu_khoa = tk.Entry(khung_tim, width=28)
        self.o_nhap_tu_khoa.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(khung_tim, text="Tìm kiếm", command=self.xu_ly_tim_kiem).grid( row=0, column=2, padx=5)
        tk.Button(khung_tim, text="Hiện tất cả", command=self.hien_thi_tat_ca).grid( row=0, column=3, padx=5)

        khung_danh_sach = tk.LabelFrame(self, text="Danh sách sách")
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_sach = tk.Listbox(khung_danh_sach, width=75, height=10)
        self.listbox_sach.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_sach.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sach.config(yscrollcommand=thanh_cuon.set)

        self.nhan_tong = tk.Label(self, text="Tổng giá trị kho sách: 0đ")
        self.nhan_tong.pack(pady=5)

    def hien_thi_danh_sach(self, danh_sach):
        """Xóa kết quả cũ rồi hiển thị danh sách mới lên Listbox."""
        self.listbox_sach.delete(0, tk.END)

        for sach in danh_sach:
            self.listbox_sach.insert(
                tk.END,
                f"{sach['MaSach']} - {sach['TenSach']} - "
                f"{sach['Gia']:.0f}đ - SL: {sach['SoLuong']}"
            )

    def hien_thi_tat_ca(self):
        self.hien_thi_danh_sach(self.danh_sach_sach)

    def xu_ly_them_sach(self):
        ma = self.o_nhap_ma.get().strip()
        ten = self.o_nhap_ten.get().strip()
        gia_text = self.o_nhap_gia.get().strip()
        soluong_text = self.o_nhap_soluong.get().strip()

        if ma == "" or ten == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ mã sách và tên sách.")
            return
        try:
            gia = float(gia_text)
            soluong = int(soluong_text)
        except ValueError:
            messagebox.showerror("Lỗi", "Giá và số lượng phải là số hợp lệ.")
            return

        if gia < 0 or soluong < 0:
            messagebox.showerror("Lỗi", "Giá và số lượng không được âm.")
            return

        Cau1.them_sach(self.danh_sach_sach, ma, ten, gia, soluong)
        self.hien_thi_danh_sach([self.danh_sach_sach[-1]])

        for o_nhap in (self.o_nhap_ma, self.o_nhap_ten, self.o_nhap_gia, self.o_nhap_soluong):
            o_nhap.delete(0, tk.END)

        tong = Cau1.tong_gia_tri_kho_sach(self.danh_sach_sach)
        self.nhan_tong.config(text=f"Tổng giá trị kho sách: {tong:,.0f}đ")

    def xu_ly_tim_kiem(self):
        tu_khoa = self.o_nhap_tu_khoa.get().strip()
        if tu_khoa == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập từ khóa cần tìm.")
            return
        ket_qua = Cau1.tim_kiem_theo_ten(self.danh_sach_sach, tu_khoa)
        self.hien_thi_danh_sach(ket_qua)
        if not ket_qua:
            messagebox.showinfo("Thông báo", "Không tìm thấy sách phù hợp.")

if __name__ == "__main__":
    ung_dung = UngDungQuanLySach()
    ung_dung.mainloop()