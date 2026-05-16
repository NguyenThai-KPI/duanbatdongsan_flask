import tkinter as tk

class MenuLeft:
    def __init__(self, parent, app_manager, dashboard_obj):
        # Tạo khu vực Menu bên trái
        self.frame_menu = tk.Frame(parent, bg="lightgray", width=200)
        self.frame_menu.pack(side="left", fill="y")

        # Đắp các Label và Button lên trên Frame này
        self.lbl_menu = tk.Label(self.frame_menu, text="MENU QUẢN LÝ", font=("Arial", 14, "bold"), bg="lightgray")
        self.lbl_menu.pack(pady=20)

        self.btn_sanpham = tk.Button(self.frame_menu, text="QUẢN LÝ BẤT ĐỘNG SẢN", width=20, bg="lightblue", font=("Arial", 10, "bold"), command=dashboard_obj.hien_thi_trang_san_pham)
        self.btn_sanpham.pack(pady=10)

        self.btn_khachhang = tk.Button(self.frame_menu, text="KHÁCH HÀNG", width=20, bg="lightgreen", font=("Arial", 10, "bold"), command=dashboard_obj.hien_thi_trang_khach_hang)
        self.btn_khachhang.pack(pady=10)

        self.btn_giaodich = tk.Button(self.frame_menu, text="GIAO DỊCH", width=20, bg="gold", font=("Arial", 10, "bold"), command=dashboard_obj.hien_thi_trang_giao_dich)
        self.btn_giaodich.pack(pady=10)

        # Nút Đăng xuất vẫn gọi về app_manager để chuyển trang như bình thường
        self.btn_dangxuat = tk.Button(self.frame_menu, text="Đăng xuất", width=20, command=app_manager.show_login_page)
        self.btn_dangxuat.pack(side="bottom", pady=20)