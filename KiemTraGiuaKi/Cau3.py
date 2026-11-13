import pandas as pd
import matplotlib.pyplot as plt

du_lieu = pd.read_csv("sach.csv")

tong_so_dau_sach = len(du_lieu)
gia_trung_binh = du_lieu["Gia"].mean()

chi_so_gia_cao_nhat = du_lieu["Gia"].idxmax()
ten_sach_gia_cao_nhat = du_lieu.loc[chi_so_gia_cao_nhat, "TenSach"]

print("Tổng số đầu sách:", tong_so_dau_sach)
print(f"Giá trung bình: {gia_trung_binh:.0f} đồng")
print("Tên sách có giá cao nhất:", ten_sach_gia_cao_nhat)

plt.bar(du_lieu["MaSach"], du_lieu["SoLuong"], color="skyblue")
plt.title("Số lượng sách tồn kho")
plt.xlabel("Mã sách")
plt.ylabel("Số lượng")
plt.tight_layout()
plt.savefig("bieudo.png")
plt.close()

sach_sap_het = du_lieu[du_lieu["SoLuong"] < 10]
sach_sap_het.to_csv("canh_bao_sach.csv", index=False)