import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from model.sanpham import SanPham

class PageSanPham:
    def __init__(self, parent):
        self.parent = parent # parent ở đây chính là cái khung màu trắng bên phải

        self.lbl_chao = tk.Label(self.parent, text="CHÀO MỪNG ĐẾN TRANG QUẢN TRỊ", font=("Arial", 20), bg="white")
        self.lbl_chao.pack(pady=20)

        # === 1. BẢNG DỮ LIỆU ===
        cac_cot = ("MaDA", "TenDuAn", "gia", "soluong", "ViTri")
        self.bang_du_lieu = ttk.Treeview(self.parent, columns=cac_cot, show="headings")

        self.bang_du_lieu.heading("MaDA", text="Mã Dự Án")
        self.bang_du_lieu.heading("TenDuAn", text="Tên Dự Án")
        self.bang_du_lieu.heading("gia", text="Mức giá")
        self.bang_du_lieu.heading("soluong", text="Số Lượng")
        self.bang_du_lieu.heading("ViTri", text="Vị Trí")
        self.bang_du_lieu.column("MaDA", width=80, anchor="center")
        self.bang_du_lieu.column("TenDuAn", width=250)

        self.bang_du_lieu.pack(fill="both", expand=True, padx=20, pady=10)
        self.bang_du_lieu.bind('<ButtonRelease-1>', self.chon_dong)

        # === 2. FORM NHẬP LIỆU ===
        self.frame_chucnang = tk.Frame(self.parent, bg="white")
        self.frame_chucnang.pack(fill="x", padx=20, pady=10)

        tk.Label(self.frame_chucnang, text="Mã Dự Án:", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txt_mada = tk.Entry(self.frame_chucnang, width=20)
        self.txt_mada.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Tên Dự Án:", bg="white").grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.txt_tenduan = tk.Entry(self.frame_chucnang, width=30)
        self.txt_tenduan.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Mức Giá:", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txt_gia = tk.Entry(self.frame_chucnang, width=20)
        self.txt_gia.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Số Lượng:", bg="white").grid(row=1, column=2, padx=10, pady=5, sticky="e")
        self.txt_soluong = tk.Entry(self.frame_chucnang, width=30)
        self.txt_soluong.grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Vị Trí:", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txt_vitri = tk.Entry(self.frame_chucnang, width=60)
        self.txt_vitri.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")

        # === 3. NÚT BẤM ===
        self.frame_nutbam = tk.Frame(self.parent, bg="white")
        self.frame_nutbam.pack(pady=10)

        self.btn_them = tk.Button(self.frame_nutbam, text="Thêm Mới", width=12, bg="lightgreen", font=("Arial", 10, "bold"), command=self.them_moi_du_an)
        self.btn_them.pack(side="left", padx=10)

        self.btn_sua = tk.Button(self.frame_nutbam, text="Cập Nhật", width=12, bg="lightblue", font=("Arial", 10, "bold"), command=self.cap_nhat_du_an)
        self.btn_sua.pack(side="left", padx=10)

        self.btn_xoa = tk.Button(self.frame_nutbam, text="Xóa", width=12, bg="salmon", font=("Arial", 10, "bold"), command=self.xoa_du_an)
        self.btn_xoa.pack(side="left", padx=10)

        self.btn_clear = tk.Button(self.frame_nutbam, text="Làm Mới", width=12, font=("Arial", 10), command=self.xoa_trang_form)
        self.btn_clear.pack(side="left", padx=10)

        # Khởi động bơm dữ liệu
        self.tai_du_lieu_vao_bang()

    # ================= CÁC HÀM XỬ LÝ LOGIC =================
    def tai_du_lieu_vao_bang(self):
        for row in self.bang_du_lieu.get_children():
            self.bang_du_lieu.delete(row)
        backend_sp = SanPham("database/sanpham.csv")
        ket_qua = backend_sp.list(page=1, page_size=100)
        for can_ho in ket_qua["data"]:
            self.bang_du_lieu.insert("", "end", values=(can_ho["MaDA"], can_ho["TenDuAn"], can_ho["gia"], can_ho["soluong"], can_ho["ViTri"]))

    def xoa_trang_form(self):
        self.txt_mada.delete(0, tk.END)
        self.txt_tenduan.delete(0, tk.END)
        self.txt_gia.delete(0, tk.END)
        self.txt_soluong.delete(0, tk.END)
        self.txt_vitri.delete(0, tk.END)

    def chon_dong(self, event):
        dong_duoc_chon = self.bang_du_lieu.focus()
        if not dong_duoc_chon: return
        gia_tri = self.bang_du_lieu.item(dong_duoc_chon, "values")
        self.xoa_trang_form()
        self.txt_mada.insert(0, gia_tri[0])
        self.txt_tenduan.insert(0, gia_tri[1])
        self.txt_gia.insert(0, gia_tri[2])
        self.txt_soluong.insert(0, gia_tri[3])
        self.txt_vitri.insert(0, gia_tri[4])

    def them_moi_du_an(self):
        ma = self.txt_mada.get().strip()
        ten = self.txt_tenduan.get().strip()
        gia = self.txt_gia.get().strip()
        sl = self.txt_soluong.get().strip()
        vitri = self.txt_vitri.get().strip()
        if ma == "" or ten == "":
            messagebox.showwarning("Cảnh báo","Chưa nhập mã dự án hoặc tên!")
            return
        try:
            with open("database/sanpham.csv", mode="a", encoding="utf-8", newline="") as file:
                csv.writer(file).writerow([ma, ten, gia, sl, vitri])
            messagebox.showinfo("Thành công", f"Đã thêm {ten}")
            self.xoa_trang_form()
            self.tai_du_lieu_vao_bang()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")

    def cap_nhat_du_an(self):
        ma = self.txt_mada.get().strip()
        if ma == "": return
        ten, gia, sl, vitri = self.txt_tenduan.get().strip(), self.txt_gia.get().strip(), self.txt_soluong.get().strip(), self.txt_vitri.get().strip()
        du_lieu_moi, tim_thay = [], False
        try:
            with open("database/sanpham.csv", mode="r", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if len(row) > 0 and row[0] == ma:
                        du_lieu_moi.append([ma, ten, gia, sl, vitri])
                        tim_thay = True
                    else:
                        du_lieu_moi.append(row)
            if not tim_thay: return
            with open("database/sanpham.csv", mode="w", encoding="utf-8", newline="") as file:
                csv.writer(file).writerows(du_lieu_moi)
            self.xoa_trang_form()
            self.tai_du_lieu_vao_bang()
            messagebox.showinfo("Thành công", "Đã cập nhật!")
        except Exception as e: pass

    def xoa_du_an(self):
        ma = self.txt_mada.get().strip()
        if ma == "": return
        if not messagebox.askyesno("Xác nhận", "Xóa vĩnh viễn?"): return
        du_lieu_giu_lai = []
        try:
            with open("database/sanpham.csv", mode="r", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if len(row) > 0 and row[0] != ma: du_lieu_giu_lai.append(row)
            with open("database/sanpham.csv", mode="w", encoding="utf-8", newline="") as file:
                csv.writer(file).writerows(du_lieu_giu_lai)
            self.xoa_trang_form()
            self.tai_du_lieu_vao_bang()
            messagebox.showinfo("Thành công", "Đã xóa!")
        except Exception as e: pass