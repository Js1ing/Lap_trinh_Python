import tkinter as tk
cua_so = tk.Tk()
cua_so.title("MAY TINH BO TUI")
cua_so.geometry("340x460")
cua_so.resizable(False, False)

khung = tk.Frame(cua_so, padx=15, pady=15)
khung.pack(fill="both", expand=True)

man_hinh = tk.Entry(khung,font=("Arial", 22),
    justify="right",bd=2, relief="solid")
man_hinh.grid(
    row=0, column=0, columnspan=4,
    sticky="nsew", pady=(0, 15), ipady=12
)
def nhap_ky_tu(ky_tu):
    man_hinh.insert(tk.END, ky_tu)
def xoa():
    man_hinh.delete(0, tk.END)

def xoa_mot_ky_tu():
    noi_dung = man_hinh.get()
    man_hinh.delete(0, tk.END)
    man_hinh.insert(0, noi_dung[:-1])

def tinh():
    bieu_thuc = man_hinh.get()
    try:
        ky_tu_hop_le = "0123456789+-*/.() "
        for ky_tu in bieu_thuc:
            if ky_tu not in ky_tu_hop_le:
                raise ValueError
        ket_qua = eval(bieu_thuc)
        man_hinh.delete(0, tk.END)
        man_hinh.insert(0, str(ket_qua))
    except:
        man_hinh.delete(0, tk.END)
        man_hinh.insert(0, "Loi phep tinh")

cac_nut = [
    ("C", 1, 0, xoa),
    ("DEL", 1, 1, xoa_mot_ky_tu),
    ("(", 1, 2, lambda: nhap_ky_tu("(")),
    (")", 1, 3, lambda: nhap_ky_tu(")")),

    ("7", 2, 0, lambda: nhap_ky_tu("7")),
    ("8", 2, 1, lambda: nhap_ky_tu("8")),
    ("9", 2, 2, lambda: nhap_ky_tu("9")),
    ("/", 2, 3, lambda: nhap_ky_tu("/")),

    ("4", 3, 0, lambda: nhap_ky_tu("4")),
    ("5", 3, 1, lambda: nhap_ky_tu("5")),
    ("6", 3, 2, lambda: nhap_ky_tu("6")),
    ("*", 3, 3, lambda: nhap_ky_tu("*")),

    ("1", 4, 0, lambda: nhap_ky_tu("1")),
    ("2", 4, 1, lambda: nhap_ky_tu("2")),
    ("3", 4, 2, lambda: nhap_ky_tu("3")),
    ("-", 4, 3, lambda: nhap_ky_tu("-")),

    ("0", 5, 0, lambda: nhap_ky_tu("0")),
    (".", 5, 1, lambda: nhap_ky_tu(".")),
    ("=", 5, 2, tinh),
    ("+", 5, 3, lambda: nhap_ky_tu("+"))
]

for ten_nut, hang, cot, lenh in cac_nut:
    nut = tk.Button(khung,text=ten_nut,font=("Arial", 15),command=lenh,
        relief="raised",bd=1,height=2)
    nut.grid(row=hang,column=cot,sticky="nsew",padx=3, pady=3)
for cot in range(4):
    khung.columnconfigure(cot, weight=1, uniform="cot")
for hang in range(1, 6):
    khung.rowconfigure(hang, weight=1, uniform="hang")
cua_so.mainloop()
