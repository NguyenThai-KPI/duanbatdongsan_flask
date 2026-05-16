import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from model.giaodich import GiaoDich


class PageGiaoDich:
    def __init__(self, parent):
        self.parent = parent

        self.lbl_chao = tk.Label(self.parent, text="QUẢN LÝ GIAO DỊCH & HỢP ĐỒNG", font=("Arial", 20), bg="white")
        self.lbl_chao.pack(pady=20)

        # === 1. BẢNG DỮ LIỆU ===
        cac_cot = ("MaGD", "MaKH", "MaDA", "Ngay", "SoTien", "TrangThai")
        self.bang_du_lieu = ttk.Treeview(self.parent, columns=cac_cot, show="headings")

        self.bang_du_lieu.heading("MaGD", text="Mã Giao Dịch")
        self.bang_du_lieu.heading("MaKH", text="Mã Khách Hàng")
        self.bang_du_lieu.heading("MaDA", text="Mã Dự Án")
        self.bang_du_lieu.heading("Ngay", text="Ngày Lập")
        self.bang_du_lieu.heading("SoTien", text="Số Tiền (VNĐ)")
        self.bang_du_lieu.heading("TrangThai", text="Trạng Thái")

        self.bang_du_lieu.column("MaGD", width=100, anchor="center")
        self.bang_du_lieu.column("MaKH", width=100, anchor="center")
        self.bang_du_lieu.column("MaDA", width=100, anchor="center")

        self.bang_du_lieu.pack(fill="both", expand=True, padx=20, pady=10)
        self.bang_du_lieu.bind('<ButtonRelease-1>', self.chon_dong)

        # === 2. FORM NHẬP LIỆU ===
        self.frame_chucnang = tk.Frame(self.parent, bg="white")
        self.frame_chucnang.pack(fill="x", padx=20, pady=10)

        tk.Label(self.frame_chucnang, text="Mã GD:", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txt_magd = tk.Entry(self.frame_chucnang, width=20)
        self.txt_magd.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Mã KH:", bg="white").grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.txt_makh = tk.Entry(self.frame_chucnang, width=20)
        self.txt_makh.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Mã Dự Án:", bg="white").grid(row=0, column=4, padx=10, pady=5, sticky="e")
        self.txt_mada = tk.Entry(self.frame_chucnang, width=20)
        self.txt_mada.grid(row=0, column=5, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Ngày Lập:", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txt_ngay = tk.Entry(self.frame_chucnang, width=20)
        self.txt_ngay.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Số Tiền:", bg="white").grid(row=1, column=2, padx=10, pady=5, sticky="e")
        self.txt_sotien = tk.Entry(self.frame_chucnang, width=20)
        self.txt_sotien.grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Trạng Thái:", bg="white").grid(row=1, column=4, padx=10, pady=5, sticky="e")
        self.txt_trangthai = tk.Entry(self.frame_chucnang, width=20)
        self.txt_trangthai.grid(row=1, column=5, padx=10, pady=5)

        # === 3. NÚT BẤM ===
        self.frame_nutbam = tk.Frame(self.parent, bg="white")
        self.frame_nutbam.pack(pady=10)

        self.btn_them = tk.Button(self.frame_nutbam, text="Lập Giao Dịch", width=15, bg="lightgreen",
                                  font=("Arial", 10, "bold"), command=self.them_moi_gd)
        self.btn_them.pack(side="left", padx=10)

        self.btn_sua = tk.Button(self.frame_nutbam, text="Cập Nhật", width=12, bg="lightblue",
                                 font=("Arial", 10, "bold"), command=self.cap_nhat_gd)
        self.btn_sua.pack(side="left", padx=10)

        self.btn_xoa = tk.Button(self.frame_nutbam, text="Hủy Giao Dịch", width=15, bg="salmon",
                                 font=("Arial", 10, "bold"), command=self.xoa_gd)
        self.btn_xoa.pack(side="left", padx=10)

        self.btn_clear = tk.Button(self.frame_nutbam, text="Làm Mới", width=12, font=("Arial", 10),
                                   command=self.xoa_trang_form)
        self.btn_clear.pack(side="left", padx=10)

        self.tai_du_lieu_vao_bang()

    # ================= LOGIC CRUD =================
    def tai_du_lieu_vao_bang(self):
        for row in self.bang_du_lieu.get_children(): self.bang_du_lieu.delete(row)
        backend_gd = GiaoDich("database/giao_dich.csv")
        for gd in backend_gd.list()["data"]:
            self.bang_du_lieu.insert("", "end", values=(gd["MaGD"], gd["MaKH"], gd["MaDA"], gd["Ngay"], gd["SoTien"],
                                                        gd["TrangThai"]))

    def xoa_trang_form(self):
        for txt in (self.txt_magd, self.txt_makh, self.txt_mada, self.txt_ngay, self.txt_sotien, self.txt_trangthai):
            txt.delete(0, tk.END)

    def chon_dong(self, event):
        dong = self.bang_du_lieu.focus()
        if not dong: return
        gia_tri = self.bang_du_lieu.item(dong, "values")
        self.xoa_trang_form()
        self.txt_magd.insert(0, gia_tri[0]);
        self.txt_makh.insert(0, gia_tri[1]);
        self.txt_mada.insert(0, gia_tri[2])
        self.txt_ngay.insert(0, gia_tri[3]);
        self.txt_sotien.insert(0, gia_tri[4]);
        self.txt_trangthai.insert(0, gia_tri[5])

    def them_moi_gd(self):
        d = [self.txt_magd.get().strip(), self.txt_makh.get().strip(), self.txt_mada.get().strip(),
             self.txt_ngay.get().strip(), self.txt_sotien.get().strip(), self.txt_trangthai.get().strip()]
        if d[0] == "" or d[1] == "" or d[2] == "": return messagebox.showwarning("Cảnh báo",
                                                                                 "Nhập đủ Mã GD, Mã KH, Mã Dự Án!")
        try:
            with open("database/giao_dich.csv", "a", encoding="utf-8", newline="") as f:
                csv.writer(f).writerow(d)
            self.xoa_trang_form();
            self.tai_du_lieu_vao_bang()
            messagebox.showinfo("Thành công", "Đã lập giao dịch mới!")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def cap_nhat_gd(self):
        ma = self.txt_magd.get().strip()
        if ma == "": return
        d = [ma, self.txt_makh.get().strip(), self.txt_mada.get().strip(), self.txt_ngay.get().strip(),
             self.txt_sotien.get().strip(), self.txt_trangthai.get().strip()]
        moi, tim_thay = [], False
        try:
            with open("database/giao_dich.csv", "r", encoding="utf-8") as f:
                for row in csv.reader(f):
                    if len(row) > 0 and row[0] == ma:
                        moi.append(d);
                        tim_thay = True
                    else:
                        moi.append(row)
            if not tim_thay: return
            with open("database/giao_dich.csv", "w", encoding="utf-8", newline="") as f:
                csv.writer(f).writerows(moi)
            self.xoa_trang_form();
            self.tai_du_lieu_vao_bang()
            messagebox.showinfo("Thành công", "Đã cập nhật giao dịch!")
        except:
            pass

    def xoa_gd(self):
        ma = self.txt_magd.get().strip()
        if ma == "": return
        if not messagebox.askyesno("Xác nhận", "Hủy giao dịch này?"): return
        giu = []
        try:
            with open("database/giao_dich.csv", "r", encoding="utf-8") as f:
                for row in csv.reader(f):
                    if len(row) > 0 and row[0] != ma: giu.append(row)
            with open("database/giao_dich.csv", "w", encoding="utf-8", newline="") as f:
                csv.writer(f).writerows(giu)
            self.xoa_trang_form();
            self.tai_du_lieu_vao_bang()
            messagebox.showinfo("Thành công", "Đã hủy giao dịch!")
        except:
            pass