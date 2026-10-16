import tkinter as tk
from tkinter import messagebox
def them_ky_tu(ky_tu):
    o_hien_thi.insert(tk.END, ky_tu)
def tinh_ket_qua():
    bieu_thuc = o_hien_thi.get()
    if bieu_thuc == "":
        messagebox.showerror("Loi", "Vui long nhap bieu thuc!")
        return
    try:
        ket_qua = eval(bieu_thuc)
        o_hien_thi.delete(0, tk.END)
        o_hien_thi.insert(tk.END, str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0!")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
def xoa_man_hinh():
    o_hien_thi.delete(0, tk.END)

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("360x460")
cua_so.resizable(False, False)

tk.Label( cua_so,text="MAY TINH BO TUI",font=("Arial", 16, "bold")
).grid(row=0, column=0, columnspan=4, pady=(20, 15))

o_hien_thi = tk.Entry(cua_so,font=("Arial", 24),justify="right",relief="solid",bd=1)
o_hien_thi.grid(row=1,column=0,columnspan=4,padx=18,pady=(0, 20),ipady=12,sticky="nsew")
cac_nut = [
    ("C", 2, 0), ("7", 2, 1), ("8", 2, 2), ("9", 2, 3),
    ("/", 3, 0), ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
    ("*", 4, 0), ("1", 4, 1), ("2", 4, 2), ("3", 4, 3),
    ("-", 5, 0), ("0", 5, 1), (".", 5, 2), ("+", 5, 3),
    ("=", 6, 0)
]
for ky_tu, hang, cot in cac_nut:
    if ky_tu == "C":
        ham_bam = xoa_man_hinh
    elif ky_tu == "=":
        ham_bam = tinh_ket_qua
    else:
        ham_bam = lambda k=ky_tu: them_ky_tu(k)
    nut = tk.Button(cua_so,text=ky_tu,font=("Arial", 16),command=ham_bam,relief="raised",bd=1)
    if ky_tu == "=":
        nut.grid( row=hang,column=0,columnspan=4, padx=18,pady=(8, 15),ipady=8,sticky="nsew")
    else:
        nut.grid(row=hang,column=cot,padx=5,pady=5,ipady=8,sticky="nsew")

for cot in range(4):
    cua_so.grid_columnconfigure(cot, weight=1, uniform="cot")
for hang in range(2, 7):
    cua_so.grid_rowconfigure(hang, weight=1, uniform="hang")

if __name__ == "__main__":
    cua_so.mainloop()
