import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from model.khachhang import KhachHang


class PageKhachHang:
    def __init__(self, parent):
        self.parent = parent

        self.lbl_chao = tk.Label(self.parent, text="QUẢN LÝ THÔNG TIN KHÁCH HÀNG", font=("Arial", 20), bg="white")
        self.lbl_chao.pack(pady=20)

        # === 1. BẢNG DỮ LIỆU ===
        cac_cot = ("MaKH", "TenKH", "SDT", "Email", "DiaChi")
        self.bang_du_lieu = ttk.Treeview(self.parent, columns=cac_cot, show="headings")

        self.bang_du_lieu.heading("MaKH", text="Mã Khách Hàng")
        self.bang_du_lieu.heading("TenKH", text="Tên Khách Hàng")
        self.bang_du_lieu.heading("SDT", text="Số Điện Thoại")
        self.bang_du_lieu.heading("Email", text="Email")
        self.bang_du_lieu.heading("DiaChi", text="Địa Chỉ")

        self.bang_du_lieu.column("MaKH", width=100, anchor="center")
        self.bang_du_lieu.column("TenKH", width=200)

        self.bang_du_lieu.pack(fill="both", expand=True, padx=20, pady=10)
        self.bang_du_lieu.bind('<ButtonRelease-1>', self.chon_dong)

        # === 2. FORM NHẬP LIỆU ===
        self.frame_chucnang = tk.Frame(self.parent, bg="white")
        self.frame_chucnang.pack(fill="x", padx=20, pady=10)

        tk.Label(self.frame_chucnang, text="Mã KH:", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txt_makh = tk.Entry(self.frame_chucnang, width=20)
        self.txt_makh.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Tên KH:", bg="white").grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.txt_tenkh = tk.Entry(self.frame_chucnang, width=30)
        self.txt_tenkh.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Số ĐT:", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txt_sdt = tk.Entry(self.frame_chucnang, width=20)
        self.txt_sdt.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Email:", bg="white").grid(row=1, column=2, padx=10, pady=5, sticky="e")
        self.txt_email = tk.Entry(self.frame_chucnang, width=30)
        self.txt_email.grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self.frame_chucnang, text="Địa Chỉ:", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txt_diachi = tk.Entry(self.frame_chucnang, width=60)
        self.txt_diachi.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")

        # === 3. NÚT BẤM ===
        self.frame_nutbam = tk.Frame(self.parent, bg="white")
        self.frame_nutbam.pack(pady=10)

        self.btn_them = tk.Button(self.frame_nutbam, text="Thêm Mới", width=12, bg="lightgreen",
                                  font=("Arial", 10, "bold"), command=self.them_moi_khach_hang)
        self.btn_them.pack(side="left", padx=10)

        self.btn_sua = tk.Button(self.frame_nutbam, text="Cập Nhật", width=12, bg="lightblue",
                                 font=("Arial", 10, "bold"), command=self.cap_nhat_khach_hang)
        self.btn_sua.pack(side="left", padx=10)

        self.btn_xoa = tk.Button(self.frame_nutbam, text="Xóa", width=12, bg="salmon", font=("Arial", 10, "bold"),
                                 command=self.xoa_khach_hang)
        self.btn_xoa.pack(side="left", padx=10)

        self.btn_clear = tk.Button(self.frame_nutbam, text="Làm Mới", width=12, font=("Arial", 10),
                                   command=self.xoa_trang_form)
        self.btn_clear.pack(side="left", padx=10)

        # Khởi động bơm dữ liệu
        self.tai_du_lieu_vao_bang()

    # ================= CÁC HÀM XỬ LÝ LOGIC =================
    def tai_du_lieu_vao_bang(self):
        for row in self.bang_du_lieu.get_children():
            self.bang_du_lieu.delete(row)

        backend_kh = KhachHang("database/khach_hang.csv")
        ket_qua = backend_kh.list(page=1, page_size=100)

        for kh in ket_qua["data"]:
            self.bang_du_lieu.insert("", "end", values=(kh["MaKH"], kh["TenKH"], kh["SDT"], kh["Email"], kh["DiaChi"]))

    def xoa_trang_form(self):
        self.txt_makh.delete(0, tk.END)
        self.txt_tenkh.delete(0, tk.END)
        self.txt_sdt.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_diachi.delete(0, tk.END)

    def chon_dong(self, event):
        dong_duoc_chon = self.bang_du_lieu.focus()
        if not dong_duoc_chon: return
        gia_tri = self.bang_du_lieu.item(dong_duoc_chon, "values")
        self.xoa_trang_form()
        self.txt_makh.insert(0, gia_tri[0])
        self.txt_tenkh.insert(0, gia_tri[1])
        self.txt_sdt.insert(0, gia_tri[2])
        self.txt_email.insert(0, gia_tri[3])
        self.txt_diachi.insert(0, gia_tri[4])

    def them_moi_khach_hang(self):
        ma = self.txt_makh.get().strip()
        ten = self.txt_tenkh.get().strip()
        sdt = self.txt_sdt.get().strip()
        email = self.txt_email.get().strip()
        diachi = self.txt_diachi.get().strip()

        if ma == "" or ten == "":
            messagebox.showwarning("Cảnh báo", "Chưa nhập mã khách hàng hoặc tên!")
            return
        try:
            with open("database/khach_hang.csv", mode="a", encoding="utf-8", newline="") as file:
                csv.writer(file).writerow([ma, ten, sdt, email, diachi])
            messagebox.showinfo("Thành công", f"Đã thêm khách hàng {ten}")
            self.xoa_trang_form()
            self.tai_du_lieu_vao_bang()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {e}")

    def cap_nhat_khach_hang(self):
        ma = self.txt_makh.get().strip()
        if ma == "": return
        ten, sdt, email, diachi = self.txt_tenkh.get().strip(), self.txt_sdt.get().strip(), self.txt_email.get().strip(), self.txt_diachi.get().strip()

        du_lieu_moi, tim_thay = [], False
        try:
            with open("database/khach_hang.csv", mode="r", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if len(row) > 0 and row[0] == ma:
                        du_lieu_moi.append([ma, ten, sdt, email, diachi])
                        tim_thay = True
                    else:
                        du_lieu_moi.append(row)
            if not tim_thay: return
            with open("database/khach_hang.csv", mode="w", encoding="utf-8", newline="") as file:
                csv.writer(file).writerows(du_lieu_moi)
            self.xoa_trang_form()
            self.tai_du_lieu_vao_bang()
            messagebox.showinfo("Thành công", "Đã cập nhật thông tin khách hàng!")
        except Exception as e:
            pass

    def xoa_khach_hang(self):
        ma = self.txt_makh.get().strip()
        if ma == "": return
        if not messagebox.askyesno("Xác nhận", "Xóa vĩnh viễn khách hàng này?"): return
        du_lieu_giu_lai = []
        try:
            with open("database/khach_hang.csv", mode="r", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if len(row) > 0 and row[0] != ma: du_lieu_giu_lai.append(row)
            with open("database/khach_hang.csv", mode="w", encoding="utf-8", newline="") as file:
                csv.writer(file).writerows(du_lieu_giu_lai)
            self.xoa_trang_form()
            self.tai_du_lieu_vao_bang()
            messagebox.showinfo("Thành công", "Đã xóa khách hàng!")
        except Exception as e:
            pass