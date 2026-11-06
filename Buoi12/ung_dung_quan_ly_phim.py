import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_phim as db

DANH_SACH_THE_LOAI = [
    "Hanh dong",
    "Tinh cam",
    "Kinh di",
    "Hoat hinh",
    "Hai",
    "Khoa hoc vien tuong",
    "Tam ly",
    "Phieu luu",
    "Lich su",
    "Khac"
]

class UngDungQuanLyPhim(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Phim ca nhan")
        self.geometry("750x560")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_phim()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ten phim:").grid(row=0, column=0, sticky="w", pady=5)

        self.o_nhap_ten_phim = tk.Entry(khung_nhap, width=35)
        self.o_nhap_ten_phim.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Dao dien:").grid(row=1, column=0, sticky="w", pady=5)

        self.o_nhap_dao_dien = tk.Entry(khung_nhap, width=35)
        self.o_nhap_dao_dien.grid( row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="The loai:").grid( row=2, column=0, sticky="w", pady=5)
        
        self.chon_the_loai = ttk.Combobox( khung_nhap, values=DANH_SACH_THE_LOAI, width=32, state="readonly")
        self.chon_the_loai.current(0)
        self.chon_the_loai.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Nam phat hanh:").grid(row=3, column=0, sticky="w", pady=5)

        self.o_nhap_nam_phat_hanh = tk.Entry(khung_nhap, width=35)
        self.o_nhap_nam_phat_hanh.grid( row=3, column=1, padx=10, pady=5)

        tk.Button( khung_nhap, text="Them phim", command=self.xu_ly_them_phim).grid(
            row=4, column=0, columnspan=2, pady=10)

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_phim = tk.Listbox(khung_danh_sach, width=90, height=15)
        self.listbox_phim.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar( khung_danh_sach, orient="vertical",command=self.listbox_phim.yview)
        thanh_cuon.pack(side="right", fill="y")

        self.listbox_phim.config( yscrollcommand=thanh_cuon.set)

        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button( khung_nut_thao_tac, text="Danh dau da xem", command=self.xu_ly_danh_dau_da_xem
        ).grid(row=0, column=0, padx=5)


        tk.Button(khung_nut_thao_tac, text="Xoa phim", command=self.xu_ly_xoa_phim
        ).grid(row=0, column=1, padx=5)


        tk.Button( khung_nut_thao_tac, text="Thong ke theo the loai", command=self.xu_ly_thong_ke
        ).grid(row=0, column=2, padx=5)


    def tai_lai_danh_sach_phim(self):
        self.listbox_phim.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_phim()

        for phim in self.danh_sach_hien_tai:
            id_phim, ten_phim, dao_dien, the_loai, nam_phat_hanh, da_xem = phim
            trang_thai = "[Da xem]" if da_xem == 1 else "[Chua xem]"
            self.listbox_phim.insert(
                tk.END,
                f"{trang_thai} {ten_phim} - {dao_dien} - "
                f"({the_loai}) - {nam_phat_hanh}"
            )


    def xu_ly_them_phim(self):
        ten_phim = self.o_nhap_ten_phim.get().strip()
        dao_dien = self.o_nhap_dao_dien.get().strip()
        the_loai = self.chon_the_loai.get()
        nam_phat_hanh = self.o_nhap_nam_phat_hanh.get().strip()
        if ten_phim == "" or dao_dien == "" or nam_phat_hanh == "":
            messagebox.showerror(
                "Loi", "Vui long nhap day du ten phim, dao dien va nam phat hanh."
            )
            return

        if not nam_phat_hanh.isdigit():
            messagebox.showerror("Loi", "Nam phat hanh phai la so nguyen.")
            return
        nam_phat_hanh = int(nam_phat_hanh)

        if nam_phat_hanh < 1888 or nam_phat_hanh > 2026:
            messagebox.showerror( "Loi", "Nam phat hanh khong hop le.")
            return

        db.them_phim( ten_phim, dao_dien, the_loai,nam_phat_hanh)
        self.o_nhap_ten_phim.delete(0, tk.END)
        self.o_nhap_dao_dien.delete(0, tk.END)
        self.o_nhap_nam_phat_hanh.delete(0, tk.END)
        self.tai_lai_danh_sach_phim()
        messagebox.showinfo(
            "Thanh cong",
            f"Da them phim: {ten_phim}"
        )


    def xu_ly_xoa_phim(self):
        lua_chon = self.listbox_phim.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot phim trong danh sach de xoa.")
            return

        id_phim = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_phim(id_phim)
        self.tai_lai_danh_sach_phim()


    def xu_ly_danh_dau_da_xem(self):
        lua_chon = self.listbox_phim.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot phim de danh dau da xem.")
            return
        
        id_phim = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_da_xem(id_phim)
        self.tai_lai_danh_sach_phim()

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_the_loai()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thong bao", "Chua co du lieu phim de thong ke.")
            return
        
        cac_the_loai = [dong[0] for dong in du_lieu_thong_ke]
        so_luong = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(8, 5))
        plt.bar( cac_the_loai, so_luong, color="cornflowerblue")
        plt.title("So luong phim theo the loai")
        plt.xlabel("The loai")
        plt.ylabel("So luong phim")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungQuanLyPhim()
    ung_dung.mainloop()
