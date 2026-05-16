import tkinter as tk
from page.menu_left import MenuLeft
from page.sanpham import PageSanPham
from page.khachhang import PageKhachHang # Import thêm mảnh Lego Khách Hàng
from page.giaodich import PageGiaoDich

class DashboardPage:
    def __init__(self, parent, app_manager):
        self.parent = parent
        self.app_manager = app_manager

        # === 1. LẮP MẢNH LEGO MENU ===
        # Truyền thêm chữ 'self' để Menu biết ai là Bo mạch chủ để ra lệnh
        self.menu = MenuLeft(self.parent, self.app_manager, self)

        # === 2. TẠO MÀN HÌNH TIVI BÊN PHẢI ===
        self.frame_noidung = tk.Frame(self.parent, bg="white")
        self.frame_noidung.pack(side="right", fill="both", expand=True)

        # Khởi động app lên thì tự động bật kênh Sản Phẩm đầu tiên
        self.hien_thi_trang_san_pham()

    def xoa_man_hinh_cu(self):
        # Thuật toán quét rác: Xóa sạch các thứ đang hiển thị trên màn hình phải
        for widget in self.frame_noidung.winfo_children():
            widget.destroy()

    def hien_thi_trang_san_pham(self):
        self.xoa_man_hinh_cu() # Tắt kênh cũ
        self.page_sp = PageSanPham(self.frame_noidung) # Bật kênh Sản Phẩm

    def hien_thi_trang_khach_hang(self):
        self.xoa_man_hinh_cu() # Tắt kênh cũ
        self.page_kh = PageKhachHang(self.frame_noidung) # Bật kênh Khách Hàng

    def hien_thi_trang_giao_dich(self):
        self.xoa_man_hinh_cu()
        self.page_gd = PageGiaoDich(self.frame_noidung)