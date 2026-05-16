import tkinter as tk
from tkinter import messagebox

from PIL.ImageShow import show

class LoginPage:
    def __init__(self, parent, app_manager):
        self.parent = parent
        self.app_manager = app_manager

        self.lbl_tieude = tk.Label(self.parent, text="ĐĂNG NHẬP HỆ THỐNG", font=("Arial", 16, "bold"))
        self.lbl_tieude.pack(pady=20)

        self.lbl_taikhoan = tk.Label(self.parent, text="Tài khoản:")
        self.lbl_taikhoan.pack(pady=5)

        self.txt_taikhoan = tk.Entry(self.parent, width=30)
        self.txt_taikhoan.pack(pady=5)

        self.lbl_matkhau = tk.Label(self.parent, text="Mật khẩu:")
        self.lbl_matkhau.pack(pady=5)

        self.txt_matkhau = tk.Entry(self.parent, width=30, show="*")
        self.txt_matkhau.pack(pady=5)

        self.btn_dangnhap = tk.Button(self.parent, text="Đăng Nhập", command=self.kiem_tra_dang_nhap, width=15, bg="light blue")
        self.btn_dangnhap.pack(pady=20)

    def kiem_tra_dang_nhap(self):

        tk_nhap = self.txt_taikhoan.get()
        mk_nhap = self.txt_matkhau.get()
        if tk_nhap == "1" and mk_nhap == "1":
            messagebox.showinfo("Đăng nhập thành công!")
            self.app_manager.show_dashboard_page()
        else:
            messagebox.showinfo("Lỗi bảo mật"," Đăng nhập thất bại!")

