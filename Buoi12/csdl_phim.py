import sqlite3
TEN_FILE_CSDL = "quan_ly_phim.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS phim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_phim TEXT NOT NULL,
            dao_dien TEXT NOT NULL,
            the_loai TEXT NOT NULL,
            nam_phat_hanh INTEGER NOT NULL,
            da_xem INTEGER NOT NULL DEFAULT 0
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_phim(ten_phim, dao_dien, the_loai, nam_phat_hanh):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        INSERT INTO phim (ten_phim, dao_dien, the_loai, nam_phat_hanh, da_xem) VALUES (?, ?, ?, ?, 0)
    """, (ten_phim, dao_dien, the_loai, nam_phat_hanh)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_phim():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(""" SELECT id, ten_phim, dao_dien, the_loai, nam_phat_hanh, da_xem
        FROM phim ORDER BY id""")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def danh_dau_da_xem(id_phim):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""UPDATE phim SET da_xem = 1 WHERE id = ? """, (id_phim,))
    ket_noi.commit()
    ket_noi.close()

def xoa_phim(id_phim):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(""" DELETE FROM phim WHERE id = ? """, (id_phim,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_the_loai():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""SELECT the_loai, COUNT(*) FROM phim GROUP BY the_loai""")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua
