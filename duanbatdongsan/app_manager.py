import tkinter as tk
from login import LoginPage
from page.dashboard import DashboardPage


class AppManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ứng dụng Đăng nhập")
        self.root.geometry("300x200")
        self.current_page = None

        self.show_login_page()

    def clear_current_page(self):
        """Xóa tất cả widget của page hiện tại"""
        if self.current_page:
            for widget in self.root.winfo_children():
                widget.destroy()

    def show_login_page(self):
        self.clear_current_page()
        self.root.geometry("400x350")
        self.current_page = LoginPage(self.root, self)

    def show_vi_du_table(self):
        """Hiển thị trang ví dụ table"""
        self.clear_current_page()
        self.root.geometry("1000x450")
        self.current_page = ViDuTablePage(self.root, self)

    def show_vi_du_tab(self):
        """Hiển thị trang ví dụ tab"""
        self.clear_current_page()
        self.current_page = ViDuTabPage(self.root, self)

    def show_vi_du_input(self):
        """Hiển thị trang ví dụ input"""
        self.clear_current_page()
        self.current_page = ViDuInputPage(self.root, self)

    def run(self):
        """Chạy ứng dụng"""
        self.root.mainloop()

    def show_dashboard_page(self):
        self.clear_current_page()
        self.root.geometry("900x500")
        self.current_page = DashboardPage(self.root, self)